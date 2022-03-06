#a string that has an 'a' followed by zero or more 'b''s.

import re

s = input()
pattern = r'ab*'

print(re.findall(pattern, s))