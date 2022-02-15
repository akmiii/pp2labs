
class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        super().__init__()
    def get_area(self):
        return self.length * self.width

length, width = map(int,input().split())  
r = Rectangle(length, width)
print(r.get_area())
