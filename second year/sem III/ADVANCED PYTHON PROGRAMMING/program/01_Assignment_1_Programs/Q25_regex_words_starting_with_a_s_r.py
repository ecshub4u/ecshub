# Q25. Find all words starting with 'a' or 's' or 'r' in a given string using RegEx
import re

txt = "sangola and solapur are cities in rajasthan or maharashtra"
pattern = r'\b[asr]\w*'
r = re.findall(pattern, txt)
print(r)
