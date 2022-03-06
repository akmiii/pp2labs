#convert a given string to snake case

import re

s = input()
pattern = r'(.)([A-Z][a-z]+)'
new_pattern = r'\1_\2'
print(re.sub(pattern, new_pattern, s))