#Problem D. 186885. Asman + Systems = Astems

n = int(input())
z = input()
if z == 'k':
    x = int(input())
    d = n / 1024
    print(round(d, x))
    
else:
    print(n * 1024)