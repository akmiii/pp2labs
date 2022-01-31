#Problem G. 195718. To decimal

def to_dec(s):
    s = s[::-1]
    n = 0
    for i in range(len(s)):
        n += int(s[i]) * (2 ** i)
    return n

s = input()
print(to_dec(s))
