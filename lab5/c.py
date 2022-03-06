#find sequences of lowercase letters joined with a underscore

import re

s = input()
pattern = r'[a-z]+_[a-z]+'

print(re.findall(pattern, s))

if re.search(pattern, s):
    print("Yes, it's here")
else:
    print("No")

