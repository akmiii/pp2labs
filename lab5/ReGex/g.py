#convert snake case string to camel case string

import re

s = input()                                         #Snake: Akmira_Privet
a = s.capitalize()
l = [i for i in a]
for i in range(len(l)-1):
    if a[i] == '_':
        if 'a' <= a[i+1] <= 'z':
            l[i+1] = chr(ord(a[i+1])-32)

new = (''.join(l))
pattern = r'(_)'
print(re.sub(pattern, '', new))                     #Camel: AkmiraPrivet