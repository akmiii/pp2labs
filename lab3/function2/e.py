from movies import *
movies = moviess()

s = input()
def getRes(l):
    res = []
    for i in movies:
        if i["category"] == s:
            res.append(i["imdb"])
    return sum(res) / len(res)
    
print(getRes(movies))