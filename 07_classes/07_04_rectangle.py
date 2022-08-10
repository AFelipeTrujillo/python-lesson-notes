class Rectangle:

    def __init__(self, b, h):
        self.b = b
        self.h = h

    def area(self):
        return self.b * self.h


r = Rectangle(12, 34)
print(f'rectangle area is {r.area()} square meters')
