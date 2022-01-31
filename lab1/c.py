#Problem C. 187587. To Lowercase

def to_lower(c):
    if ord('A') <= ord(c) <= ord('Z'):
        return chr(ord(c) + 32)
    return c

s = input()
d = ""
for c in s:
    d += to_lower(c)

print(d)
