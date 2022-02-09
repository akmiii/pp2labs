#Problem K. 195846. Final essay

s = input()
s = s.replace(',', '').replace('.', '').replace('!', '').replace('?', '').split()
#print(s)
l = []
for i in s:
    if i not in l:
        l.append(i)

print(len(l))
l.sort()
print(*l, sep = '\n')