#filter_prime

from math import sqrt

numbers = list(map(int, input().split()))

def isPrime(n):
    if n == 1 or n == 0:
        return False
    for i in range(2, int(sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

def filter(num):
    arr = []
    for i in num:
        if isPrime(i):
            arr.append(i)
    return(arr)
    
print(*filter(numbers))