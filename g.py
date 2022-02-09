#Problem G. Demon slayer

num_d = int(input())
d = dict()
for i in range(num_d):
    name, weak = input().split()
    if weak in d:
        d[weak] = int(d[weak]) + 1
    else:
        d[weak] = 1
#print(d)

num_h = int(input())
for i in range(num_h):
    name, weak, num = input().split()
    if weak in d.keys():
        d[weak] = int(d[weak]) - int(num)

sum = 0
for i in d.values():
    if i > 0:
        sum += i
print("Demons left: ", sum) 