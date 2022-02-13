from movies import *
movies = moviess()

def getRes(l):
    res = []
    for i in movies:
        res.append(i["imdb"])
    return sum(res) / len(movies)

print(getRes(movies))
