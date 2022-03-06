#a string that has an 'a' followed by two to three 'b'

import re

s = input()
pattern = r'ab{2,3}'

print(bool(re.search(pattern, s)))