#!/usr/bin/env python3
r"""
ECSHub automatic updater

What this script does:
1. Scans ONLY:
   - first year/
   - second year/
   - third year/
2. Updates ONLY the existing `const fileTree = ...;` data inside index.html.
3. Creates an HTML backup of the old index.html in E:\backups.
4. Automatically generates/updates sitemap.xml from the files inside
   the three folders above.
5. Does NOT regenerate or replace the rest of index.html.

Run from anywhere:
    python update.py

Recommended location:
    C:\Users\rohan\Desktop\ecshub\update.py
"""

from pathlib import Path
from datetime import datetime
import json
import re
import sys
from xml.sax.saxutils import escape

# ============================================================
# CONFIGURATION
# ============================================================

# The script is kept in the ECSHub root, beside index.html.
ROOT = Path(__file__).resolve().parent
INDEX_FILE = ROOT / "index.html"
SITEMAP_FILE = ROOT / "sitemap.xml"

# Backups stay OUTSIDE the repository.
BACKUP_DIR = Path(r"E:\backups")

# IMPORTANT: only these three top-level folders are scanned.
SCAN_ROOTS = [
    "first year",
    "second year",
    "third year",
]

# Your GitHub Pages project URL.
# If your live website URL is different, change ONLY this line.
SITE_URL = "https://ecshub4u.github.io/ecshub/"

# Files/folders that should not appear in the generated tree/sitemap.
IGNORED_NAMES = {
    ".git",
    ".github",
    ".gitignore",
    ".gitattributes",
    ".DS_Store",
    "Thumbs.db",
    "__pycache__",
}

IGNORED_EXTENSIONS = {
    ".tmp",
    ".temp",
    ".bak",
    ".swp",
    ".swo",
}

# Known extensions. Unknown extensions are still included as "file".
EXTENSION_TYPES = {
    ".pdf": "pdf",
    ".doc": "doc",
    ".docx": "docx",
    ".ppt": "ppt",
    ".pptx": "pptx",
    ".txt": "txt",
    ".html": "html",
    ".htm": "html",
    ".js": "js",
    ".css": "css",
    ".py": "py",
    ".c": "c",
    ".h": "h",
    ".cpp": "cpp",
    ".cc": "cpp",
    ".cxx": "cpp",
    ".hpp": "cpp",
    ".java": "java",
    ".sql": "sql",
    ".json": "json",
    ".xml": "xml",
    ".csv": "csv",
    ".jpg": "jpg",
    ".jpeg": "jpg",
    ".png": "png",
    ".gif": "gif",
    ".webp": "webp",
    ".svg": "svg",
    ".bmp": "bmp",
    ".ico": "ico",
    ".exe": "exe",
    ".zip": "zip",
    ".rar": "rar",
    ".7z": "7z",
}

SUBJECT_ICONS = {
    "aptitude": "fa-solid fa-calculator",
    "constitution of india": "fa-solid fa-scale-balanced",
    "digital electronics and microprocessors": "fa-solid fa-microchip",
    "english for communication-i": "fa-solid fa-comments",
    "english for communication-ii": "fa-solid fa-comments",
    "introduction to iks in science": "fa-solid fa-atom",
    "introduction to web design": "devicon-html5-plain",
    "numerical methods": "fa-solid fa-square-root-variable",
    "office automation": "fa-solid fa-briefcase",
    "oop’s with c++-i": "devicon-cplusplus-plain",
    "oops with c++-i": "devicon-cplusplus-plain",
    "oops with c++-ii": "devicon-cplusplus-plain",
    "advanced web designing": "devicon-bootstrap-plain",
    "advanced python programming": "fa-brands fa-python",
    "python programming-i": "fa-brands fa-python",
    "python programming -ii": "fa-brands fa-python",
    "database management systems": "fa-solid fa-database",
    "data structures using c++": "devicon-cplusplus-plain",
    "operating systems": "fa-solid fa-server",
    "reading texts in indian english-i": "fa-solid fa-book-open",
    "reading texts in indian english-ii": "fa-solid fa-book-open",
    "statistics for data science  i": "fa-solid fa-chart-line",
    "statistics for data science - ii": "fa-solid fa-chart-line",
    "yoga education": "fa-solid fa-om",
    "computer networks": "fa-solid fa-network-wired",
    "core java": "fa-brands fa-java",
    "relational database management system": "fa-solid fa-table-list",
    "software testing and quality assurance": "fa-solid fa-bug",
    "software engineering": "fa-solid fa-gears",
    "environmental studies": "fa-solid fa-leaf",
    "introduction to microcontroller and embedded system": "fa-solid fa-robot",
    "soft skin and personality development": "fa-solid fa-user-tie",
}


# ============================================================
# FILE TREE
# ============================================================

def is_ignored(path: Path) -> bool:
    return (
        path.name in IGNORED_NAMES
        or path.name.startswith(".")
        or (
            path.is_file()
            and path.suffix.lower() in IGNORED_EXTENSIONS
        )
    )


def children(path: Path):
    items = [p for p in path.iterdir() if not is_ignored(p)]
    return sorted(
        items,
        key=lambda p: (p.is_file(), p.name.casefold())
    )


def file_type(path: Path) -> str:
    return EXTENSION_TYPES.get(path.suffix.lower(), "file")


def folder_tree(path: Path):
    result = {"type": "folder"}

    for p in children(path):
        if p.is_dir():
            result[p.name] = folder_tree(p)
        else:
            result[p.name] = file_type(p)

    return result


def subject_tree(path: Path):
    icon = SUBJECT_ICONS.get(
        path.name.casefold(),
        "fa-solid fa-folder-open"
    )

    files = {}

    for p in children(path):
        if p.is_dir():
            files[p.name] = folder_tree(p)
        else:
            files[p.name] = file_type(p)

    return {
        "type": "subject",
        "icon": icon,
        "files": files,
    }


def year_tree(path: Path):
    result = {}

    for p in children(path):
        if p.is_dir():

            # Existing ECSHub structure:
            # first year/
            #   sem I/
            #   sem II/
            if p.name.casefold().startswith("sem "):
                semester = {}

                for item in children(p):
                    if item.is_dir():
                        semester[item.name] = subject_tree(item)
                    else:
                        semester[item.name] = file_type(item)

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


# ============================================================
# INDEX.HTML UPDATE
# ============================================================

def update_index(original: str, tree: dict) -> str:
    """
    Replace ONLY:
        const fileTree = ...;

    Everything else in index.html remains untouched.
    """

    pattern = re.compile(
        r"(const\s+fileTree\s*=\s*)(.*?)(;)",
        re.DOTALL,
    )

    match = pattern.search(original)

    if not match:
        raise RuntimeError(
            "Could not find `const fileTree = ...;` in index.html.\n"
            "No index.html changes were made."
        )

    data = json.dumps(
        tree,
        ensure_ascii=False,
        separators=(",", ":"),
    )

    replacement = match.group(1) + data + match.group(3)

    return (
        original[:match.start()]
        + replacement
        + original[match.end():]
    )


# ============================================================
# SITEMAP
# ============================================================

def url_encode_path(relative_path: Path) -> str:
    """
    Encode a repository path for a URL while preserving spaces and
    special characters safely.

    Uses urllib.parse.quote so URLs such as:
      OOP’S with C++-I
      Previous Year Question Paper
    become valid sitemap URLs.
    """
    from urllib.parse import quote

    return quote(
        relative_path.as_posix(),
        safe="/:@-._~!$&'()*+,;=",
    )


def collect_sitemap_urls():
    """
    Include the homepage plus every non-ignored file inside the
    three allowed scan roots.

    This includes HTML, PDF, DOCX, images, source files, EXE files,
    and other extensions present in those folders.
    """

    urls = {SITE_URL.rstrip("/") + "/"}

    for root_name in SCAN_ROOTS:
        root = ROOT / root_name

        if not root.exists() or not root.is_dir():
            continue

        for path in root.rglob("*"):
            if not path.is_file():
                continue

            if is_ignored(path):
                continue

            relative = path.relative_to(ROOT)
            urls.add(
                SITE_URL.rstrip("/")
                + "/"
                + url_encode_path(relative)
            )

    return sorted(urls)


def generate_sitemap():
    urls = collect_sitemap_urls()

    today = datetime.now().date().isoformat()

    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]

    for url in urls:
        lines.append("  <url>")
        lines.append(f"    <loc>{escape(url)}</loc>")
        lines.append(f"    <lastmod>{today}</lastmod>")
        lines.append("  </url>")

    lines.append("</urlset>")

    sitemap_content = "\n".join(lines) + "\n"

    old_content = (
        SITEMAP_FILE.read_text(encoding="utf-8")
        if SITEMAP_FILE.exists()
        else ""
    )

    changed = old_content != sitemap_content

    if changed:
        SITEMAP_FILE.write_text(
            sitemap_content,
            encoding="utf-8",
        )

    return changed, len(urls)


# ============================================================
# BACKUP
# ============================================================

def create_index_backup(original: str):
    """
    Backup format:
        index-24Aug26-20hr04min.html

    Backups are kept on E:\backups, not in the repository.
    """

    BACKUP_DIR.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime(
        "%d%b%y-%Hhr%Mmin"
    )

    backup = BACKUP_DIR / f"index-{timestamp}.html"

    # If the script is run more than once in the same minute,
    # avoid overwriting the previous backup while keeping the
    # requested date/time format.
    counter = 2
    while backup.exists():
        backup = (
            BACKUP_DIR
            / f"index-{timestamp}-{counter}.html"
        )
        counter += 1

    backup.write_text(
        original,
        encoding="utf-8",
    )

    return backup


# ============================================================
# MAIN
# ============================================================

def main():
    print("==============================================")
    print(" ECSHub - Automatic Website Updater")
    print("==============================================")
    print()

    if not INDEX_FILE.exists():
        print("ERROR: index.html was not found.")
        print(f"Expected location: {INDEX_FILE}")
        sys.exit(1)

    print("Scanning ONLY:")
    for name in SCAN_ROOTS:
        print(f"  {name}/")

    print()

    # Read current index.html.
    original_index = INDEX_FILE.read_text(
        encoding="utf-8"
    )

    # Build new tree.
    tree = build_file_tree()

    # Prepare updated index.html.
    updated_index = update_index(
        original_index,
        tree,
    )

    index_changed = updated_index != original_index

    # Generate/update sitemap.
    sitemap_changed, url_count = generate_sitemap()

    # Nothing changed.
    if not index_changed and not sitemap_changed:
        print("No changes detected.")
        print("index.html and sitemap.xml are already up to date.")
        print()
        return

    # Back up the OLD index.html before replacing it.
    backup = None

    if index_changed:
        backup = create_index_backup(
            original_index
        )

        INDEX_FILE.write_text(
            updated_index,
            encoding="utf-8",
        )

    print("SUCCESS!")
    print()

    if index_changed:
        print("index.html: UPDATED")
        print(f"Backup: {backup}")
    else:
        print("index.html: No change")

    if sitemap_changed:
        print(f"sitemap.xml: UPDATED ({url_count} URLs)")
    else:
        print("sitemap.xml: No change")

    print()
    print("The script scans ONLY first year/, second year/,")
    print("and third year/.")
    print()
    print("The rest of index.html is NOT regenerated.")
    print("Your existing HTML, CSS, JavaScript, SEO,")
    print("Google verification tag, etc. are preserved.")
    print()
    print("Next commands:")
    print("  git status")
    print("  git diff -- index.html sitemap.xml")
    print("  git add .")
    print('  git commit -m "Update study material"')
    print("  git push origin main")
    print()


if __name__ == "__main__":
    main()
