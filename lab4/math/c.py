#the area of regular polygon

from math import floor, tan, pi
n = float(input("Input number of sides: "))
a = float(input("Input the length of a side: "))
area = (n * a ** 2)/(4*tan(pi/n))
print(f'The area of the polygon is: {floor(area)}')
