# Q24. Replace all white spaces by "*" using re.sub() (From Professor's Notes)
import re

string = "sangola mahavidyala sangola Tal:sangola Dist:solapur"
pattern = r'\s+'
replace = '*'
new_string = re.sub(pattern, replace, string)
print(new_string)
