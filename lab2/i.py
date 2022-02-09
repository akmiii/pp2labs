#Problem I. 77244. Discs

l = []
res = []
n = int(input())
for i in range(n):
    s = input().split()
    if s[0] == '1':
        l.append(s[1])
    else:
        if s[0] == '2':
            res.append(l[0])
            l.pop(0)

#print(l)
print(*res)
