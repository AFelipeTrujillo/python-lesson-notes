from Square import *
from Rectangle import *

s = Square(10,'red')
print(s.area())
print(s.color)
print(Square.mro())
print(s)
print('Rectangle'.center(50,'='))
r = Rectangle(10,30,'green')
print(r.area())
print(r)
