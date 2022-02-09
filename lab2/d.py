#Problem D. 188131. Tsunami

n = int(input())
if n % 2 != 0:
    for i in range(n):
        for j in range(n):
            if i + j < n-1:
                print('.', sep = '', end = '')
            else:
                print('#', sep='', end= '')
        print()
else:
    for i in range(n):
        for j in range(n):
            if i >= j:
                print('#', sep= '', end= '')
            else:
                print('.', sep= '', end= '')
        print()
