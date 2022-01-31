#Problem H. 187532. First and last occurrence

s = input()
c = input()
if c in s:
    print(s.find(c), end = ' ')
    if s.rfind(c) != s.find(c):
        print(s.rfind(c))





'''   #with list

s = input()
c = input()
res = []
for i in range(len(s)):
    if c == s[i]:
        res.append(i)
if len(res) == 1:
    print(res[0])
else:
    print(res[0], res[-1])
'''