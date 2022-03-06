#replace all occurrences of space, comma, or dot with a colon

import re

s = input()
pattern = r'[\s,\.]'
print(re.sub(pattern, ':', s))