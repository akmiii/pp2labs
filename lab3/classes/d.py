from math import sqrt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        return self.x, self.y
    def move(self, x, y):
        self.x = x
        self.y = y
    def dist(self, p2):
        return sqrt((self.x - p2.x)**2 + (self.y - p2.y)**2)

x, y = map(int,input().split()) 
x1, y1 = map(int,input().split())
p1 = Point(x, y)
p2 = Point(x1, y1)
print(p1.show())
#p1.move(1, 3)
#print(p1.show())
print(p1.dist(p2))