from math import sqrt
numbers = [int(i) for i in input().split()]
def isPrime(n):
    if n == 1 or n == 0:
        return False
    for i in range(2, int(sqrt(n)+1)):
        if n % i == 0:
            return False
    return True
res = list(filter(lambda x: isPrime(x), numbers))
print(*res)