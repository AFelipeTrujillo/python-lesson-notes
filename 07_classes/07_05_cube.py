class Cube:

    def __init__(self, b, h, d):
        self.b = b
        self.h = h
        self.d = d

    def area(self):
        return self.d * self.h * self.b


c = Cube(3, 5, 7)
print(f'{Cube.area(c)}')
