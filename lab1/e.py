#Problem E. 188812. Gunner

n, f = map(int, input().split())

def isPrime(n):
    if n == 1 or n == 0:
        return False
    for i in range(2, n//2):
        if n % i == 0:
            return False
    return True
    
if isPrime(n) and n < 500 and f % 2 == 0:
    print("Good job!")
else:
    print("Try next time!")