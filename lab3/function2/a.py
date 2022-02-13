from movies import *
movies = moviess()

s = input()
def getRes(s):
    for i in movies:
        if i["name"] == s:
            if i["imdb"] > 5.5:
                return True
            return False
print(getRes(s))