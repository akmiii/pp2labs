from movies import *
movies = moviess()

s = input()
def getRes(s):
    res = []
    for i in movies:
        if i["category"] == s:
            res.append(i["name"])
    return res
    
print(*getRes(s), sep = '\n')