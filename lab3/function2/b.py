from movies import *
movies = moviess()

def getRes(l):
    res = []
    for i in movies:
        if i["imdb"] > 5.5:
            res.append(i["name"]) 
    return res
print(getRes(movies))
