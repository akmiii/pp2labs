#the square of all numbers from (a) to (b)

def squares(a, b):
    for i in range(a, b+1):
        yield i**2
        
a = int(input())
b = int(input())
sq = squares(a, b)
l = [next(sq) for _ in range(a, b+1)]
print(*l)