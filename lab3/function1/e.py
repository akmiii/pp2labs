#permutations
       #a, b, c  #0     #2
def getPerm(a, start, end):
    if start == end:
        print(''.join(a))
    else:               #1      #3
        for i in range(start, end+1):
            #a[1], a[0]    = a[0], a[1]
            a[start], a[i] = a[i], a[start]
            #          1       2
            getPerm(a, start+1, end)
            a[start], a[i] = a[i], a[start]     #заново поставить на место
 
s = input()
a = list(s)
getPerm(a, 0, len(s)-1)
    
