#a string that has an 'a' followed by anything, ending in 'b'

import re

s = input()
pattern = r'a[a-zA-Z0-9]+b$'

print(re.findall(pattern, s))

if re.search(pattern, s):
    print("Yes, it's here")
else:
    print("No")