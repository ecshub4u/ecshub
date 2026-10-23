# Program: Grouping () In Regular Expressions
# Question: Explain the use of grouping () in regular expressions with an example.

import re

# Parentheses () group sub-patterns. (a|b|c)xz matches a or b or c followed by xz
print(re.findall("(a|b|c)xz", "axz cabxz"))
m = re.search("(a|b|c)xz", "abxz")
print(m.group(), m.span())
