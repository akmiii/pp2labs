#unique elements

l = [i for i in input().split()]

def uniq(arr):
    res = []
    for i in arr:
        if i not in res:
            res.append(i)
    return res

print(*uniq(l))