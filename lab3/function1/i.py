#the volume of a sphere

from math import pi

r = int(input())

def getRes(r):
    return (4*pi*(r**3) / 3)
print(getRes(r))