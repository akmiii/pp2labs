#returns all numbers from (n) down to 0

def gener(n):
    for i in range(n, -1, -1):
        yield i

n = int(input())
num = gener(n)
l = [next(num) for _ in range(n, -1, -1)]
print(*l)