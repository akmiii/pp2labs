#Problem B. 187378. Maximum product of two elements

n = int(input())
l = list(map(int, input().split()))
res = []
for i in range(len(l) - 1):
    for j in range(i+1, len(l)):
        res.append(l[i] * l[j])
mx = 0
for i in res:
    mx = max(mx, i)
print(mx)