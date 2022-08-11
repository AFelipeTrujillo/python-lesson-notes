from Shape import *
from Color import *


class Square(Shape, Color):
    def __init__(self, h, color):
        Shape.__init__(self, h,h)
        Color.__init__(self, color)

    def area(self):
        return self.h ** 2
