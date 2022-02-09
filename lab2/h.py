#Problem H. Closest point
 
from math import sqrt
x, y = map(int, input().split())

def distance(num):
    return sqrt((x-num[0])**2 + (y-num[1]) **2)

n = int(input())
l = []
for i in range(n):
    x1, y1 = map(int, input().split())
    l.append((x1, y1))
#print(l)

arr = sorted(l, key = distance)
#print(arr)
for c in arr:
    print(c[0], c[1])




'''for i in range(n):
    x1, y1 = list(map(int, input().split()))
    d = sqrt((x1-x)**2 + (y1-y) **2)
    l.append(d)
    dic[d] = x1, y1
print(l)
print("-"*20)
for key, value in dic.items():
    print(*value)'''
