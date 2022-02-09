#Problem F. 196670. Compensations

d = dict()
n = int(input())
for i in range(n):
    name, money = map(str, input().split())
    if name not in d.keys():
        d[name] = int(money)
    else:
        d[name] += int(money)
#print(d)
mx = 0
for key, value in d.items():
    if value > mx:
        mx = value
#print(mx)
for key, value in sorted(d.items()):
    if value == mx:
        print(key, "is lucky!")
    else:
        print(key, "has to receive", mx - value, "tenge")