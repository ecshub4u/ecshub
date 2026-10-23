# Program: Replace White Spaces With Star
# Question: Consider a string "sangola mahavidyala sangola Tal:sangola Dist:solapur ". Replace all
# white spaces by "*" use appropriate regex method.

import re

s = "sangola mahavidyala sangola Tal:sangola Dist:solapur "
result = re.sub(r"\s", "*", s)         # \s matches whitespace
print(result)
