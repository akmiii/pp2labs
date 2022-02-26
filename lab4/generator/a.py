#the squares of numbers up to some number N

def gener(n, k = 1):
    for _ in range(n):
        yield k ** 2
        k += 1

n = int(input())
sq = gener(n)
l = [next(sq) for _ in range(n)]
print(*l)