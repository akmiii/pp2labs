#words reversed

s = input().split()

def getRev(s):
    l = []
    for i in s:
        if i == len(s):
            return
        else:
            l.append(i)
    return(l[::-1])

print(*getRev(s))