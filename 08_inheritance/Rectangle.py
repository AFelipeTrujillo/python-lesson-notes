from Shape import *
from Color import *

class Rectangle(Shape, Color):

    def __init__(self, h, w, color):
        Shape.__init__(self, h, w)
        Color.__init__(self, color)

    def area(self):
        return self.h * self.w

    def __str__(self):
        return f'{Shape.__str__(self)} {Color.__str__(self)}'