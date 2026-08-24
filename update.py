#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime
import json
import re
import sys

# Keep this script in the ECSHub repository root, beside index.html.
ROOT = Path(__file__).resolve().parent
INDEX_FILE = ROOT / "index.html"

# Backups are stored OUTSIDE the ECSHub repository.
BACKUP_DIR = Path(r"E:\backups")

# ONLY these three folders are scanned.
SCAN_ROOTS = ["first year", "second year", "third year"]

# Internal/system files and temporary files are ignored.
IGNORED_NAMES = {
    ".git", ".github", ".gitignore", ".gitattributes",
    ".DS_Store", "Thumbs.db", "__pycache__"
}
IGNORED_EXTENSIONS = {".tmp", ".temp", ".bak", ".swp", ".swo"}

# Known file types. Any unknown extension is still included as "file".
EXTENSION_TYPES = {
    ".pdf":"pdf", ".doc":"doc", ".docx":"docx",
    ".ppt":"ppt", ".pptx":"pptx",
    ".txt":"txt", ".html":"html", ".htm":"html",
    ".js":"js", ".css":"css", ".py":"py",
    ".c":"c", ".h":"h", ".cpp":"cpp", ".cc":"cpp",
    ".cxx":"cpp", ".hpp":"cpp", ".java":"java",
    ".sql":"sql", ".json":"json", ".xml":"xml", ".csv":"csv",
    ".jpg":"jpg", ".jpeg":"jpg", ".png":"png", ".gif":"gif",
    ".webp":"webp", ".svg":"svg", ".bmp":"bmp", ".ico":"ico",
    ".exe":"exe", ".zip":"zip", ".rar":"rar", ".7z":"7z"
}

SUBJECT_ICONS = {
    "aptitude":"fa-solid fa-calculator",
    "constitution of india":"fa-solid fa-scale-balanced",
    "digital electronics and microprocessors":"fa-solid fa-microchip",
    "english for communication-i":"fa-solid fa-comments",
    "english for communication-ii":"fa-solid fa-comments",
    "introduction to iks in science":"fa-solid fa-atom",
    "introduction to web design":"devicon-html5-plain",
    "numerical methods":"fa-solid fa-square-root-variable",
    "office automation":"fa-solid fa-briefcase",
    "oop’s with c++-i":"devicon-cplusplus-plain",
    "oops with c++-i":"devicon-cplusplus-plain",
    "oops with c++-ii":"devicon-cplusplus-plain",
    "advanced web designing":"devicon-bootstrap-plain",
    "advanced python programming":"fa-brands fa-python",
    "python programming-i":"fa-brands fa-python",
    "python programming -ii":"fa-brands fa-python",
    "database management systems":"fa-solid fa-database",
    "data structures using c++":"devicon-cplusplus-plain",
    "operating systems":"fa-solid fa-server",
    "reading texts in indian english-i":"fa-solid fa-book-open",
    "reading texts in indian english-ii":"fa-solid fa-book-open",
    "statistics for data science  i":"fa-solid fa-chart-line",
    "statistics for data science - ii":"fa-solid fa-chart-line",
    "yoga education":"fa-solid fa-om",
    "computer networks":"fa-solid fa-network-wired",
    "core java":"fa-brands fa-java",
    "relational database management system":"fa-solid fa-table-list",
    "software testing and quality assurance":"fa-solid fa-bug",
    "software engineering":"fa-solid fa-gears",
    "environmental studies":"fa-solid fa-leaf",
    "introduction to microcontroller and embedded system":"fa-solid fa-robot",
    "soft skin and personality development":"fa-solid fa-user-tie",
}

def ignored(path):
    return (
        path.name in IGNORED_NAMES
        or path.name.startswith(".")
        or (path.is_file() and path.suffix.lower() in IGNORED_EXTENSIONS)
    )

def children(path):
    items = [p for p in path.iterdir() if not ignored(p)]
    return sorted(items, key=lambda p: (p.is_file(), p.name.casefold()))

def file_type(path):
    return EXTENSION_TYPES.get(path.suffix.lower(), "file")

def folder_tree(path):
    result = {"type": "folder"}
    for p in children(path):
        result[p.name] = folder_tree(p) if p.is_dir() else file_type(p)
    return result

def subject_tree(path):
    icon = SUBJECT_ICONS.get(path.name.casefold(), "fa-solid fa-folder-open")
    files = {}
    for p in children(path):
        files[p.name] = folder_tree(p) if p.is_dir() else file_type(p)
    return {"type": "subject", "icon": icon, "files": files}

def year_tree(path):
    result = {}
    for p in children(path):
        if p.is_dir():
            if p.name.casefold().startswith("sem "):
                semester = {}
                for item in children(p):
                    semester[item.name] = (
                        subject_tree(item) if item.is_dir()
                        else file_type(item)
                    )
                result[p.name] = semester
            else:
                result[p.name] = folder_tree(p)
        else:
            result[p.name] = file_type(p)
    return result

def build_file_tree():
    tree = {}
    for name in SCAN_ROOTS:
        path = ROOT / name
        if not path.exists():
            print(f"WARNING: {name}/ not found")
            tree[name] = {}
        elif not path.is_dir():
            print(f"WARNING: {name} exists but is not a folder")
            tree[name] = {}
        else:
            tree[name] = year_tree(path)
    return tree

def update_index(original, tree):
    # Replace ONLY the existing const fileTree = ...; declaration.
    pattern = re.compile(
        r"(const\s+fileTree\s*=\s*)(.*?)(;)",
        re.DOTALL
    )
    match = pattern.search(original)

    if not match:
        raise RuntimeError(
            "Could not find `const fileTree = ...;` in index.html. "
            "No changes were made."
        )

    data = json.dumps(tree, ensure_ascii=False, separators=(",", ":"))
    replacement = match.group(1) + data + match.group(3)

    return original[:match.start()] + replacement + original[match.end():]

def main():
    print("========================================")
    print(" ECSHub - Automatic index.html Updater")
    print("========================================")
    print()

    if not INDEX_FILE.exists():
        print("ERROR: index.html is not beside this script.")
        sys.exit(1)

    print("Scanning ONLY:")
    for name in SCAN_ROOTS:
        print("  " + name + "/")
    print()

    original = INDEX_FILE.read_text(encoding="utf-8")
    tree = build_file_tree()
    updated = update_index(original, tree)

    if updated == original:
        print("No changes detected.")
        print("index.html is already up to date.")
        return

    # Create E:\backups automatically if needed.
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)

    # Backup format:
    # index-24Aug26-20hr04min.html
    timestamp = datetime.now().strftime("%d%b%y-%Hhr%Mmin")
    backup = BACKUP_DIR / f"index-{timestamp}.html"
    backup.write_text(original, encoding="utf-8")

    # Update the real index.html.
    INDEX_FILE.write_text(updated, encoding="utf-8")

    print("SUCCESS!")
    print()
    print("index.html has been updated.")
    print(f"Backup created: {backup}")
    print()
    print("Only `const fileTree = ...;` was changed.")
    print("Your HTML, CSS, JavaScript, SEO, Google verification,")
    print("and other website code are NOT regenerated.")
    print()
    print("Now check:")
    print("  git diff -- index.html")
    print()
    print("Then:")
    print("  git add .")
    print('  git commit -m "Update study material"')
    print("  git push origin main")
    print()

if __name__ == "__main__":
    main()
