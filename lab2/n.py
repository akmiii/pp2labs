#Problem N. 194739. We got stronger

l = []
while (True):
    x = int(input())
    if x == 0:
        break
    else:
        l.append(x)
#print(l)
arr = []

if len(l) % 2 == 0:
    for i in range(len(l)//2):
        arr.append(l[i] + l[len(l)-i-1])
else:
    for i in range(len(l)//2 + 1):
        arr.append(l[i] + l[len(l)-i-1])
    arr[len(arr)-1] -= l[i]

print(*arr)
