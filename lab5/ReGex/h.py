#split a string at uppercase letters

import re

s = input()
pattern = r'(?=[A-Z])'

l = re.split(pattern, s)
del l[0]
print(*l)