#print the even numbers between 0 and n in comma separated

def generator(seq):
    for i in seq:
        if i % 2 == 0:
            yield i

n = int(input())
l = [i for i in range(n+1)]
res = []
for i in generator(l):
    res.append(i)

print(*res, sep=',')