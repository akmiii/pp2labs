#the numbers, which are divisible by 3 and 4

def generator(seq):
    for i in seq:
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input())
l = [i for i in range(n+1)]
res = []
for i in generator(l):
    res.append(i)

print(*res, sep= ',')