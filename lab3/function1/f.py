#words reversed

s = input().split()

def getRes(s):
    l = []
    for i in s:
        if i == len(s):
            return
        else:
            l.append(i)
    return(l[::-1])

print(*getRes(s))