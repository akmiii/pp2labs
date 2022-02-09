#Problem A. 190087. Asmay

l = []
for i in input().split():
    l.append(i)             #2 3 1 1 4

last = len(l)-1             #last = 4

for i in range(len(l)-2, -1, -1):   #2 3<-1<-1
    if (i + int(l[i])) >= last:     #3+1 >= 4        2+1 >= 3
        last = i                    #last = 3        last = 2

if last == 0:
    print('1')
else:
    print('0')