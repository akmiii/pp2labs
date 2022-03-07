#multiply all the numbers in a list
from functools import reduce

def mult(a, b):
    return a * b

l = list(map(int, input().split()))

print(reduce(mult, l))