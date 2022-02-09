#Problem C. 187698. Diagonal x 

n = int(input())
for i in range(n):
    for j in range(n):
        if i == j:
            print(i * j, end = ' ')
        elif i == 0:               #filling 1st row [0, 1, 2,3, ...]
            print(j, end = ' ')     
        elif j == 0:               #filling 1sr column [1, 2, 3 ...]
            print(i, end = ' ')
        else:
            print('0', end = ' ')
    print()
    