from abc import ABC, abstractmethod


class Shape(ABC):

    def __init__(self, h, w):
        self._h = h
        self._w = w

    @abstractmethod
    def area(self):
        pass


class Square(Shape):

    def area(self):
        return self._h ** 2

    def __init__(self, h):
        self._h = h
        super(Square, self).__init__(h, h)
        pass


c = Square(10)
print(c.area())

