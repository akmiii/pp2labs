class Shape:
    def get_area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length
    def get_area(self):
        return self.length**2

s = Square(int(input()))
#a = Shape()
print(s.get_area())
#print(a.get_area())