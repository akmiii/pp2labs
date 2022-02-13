#Histogram
l = [int(i) for i in input().split()]

def hist(l):
    res = []
    for i in range(len(l)):
        res.append('*'*l[i])
    return res

print(*hist(l), sep= '\n')