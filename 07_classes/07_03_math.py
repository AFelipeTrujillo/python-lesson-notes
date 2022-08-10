class Math:
    """
    Math Class
    """

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b

    def subtraction(self):
        return self.a - self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        return self.a / self.b


m = Math(5, 4)
print(f'sum {m.sum()}')
print(f'subtraction {m.subtraction()}')
print(f'multiplication {m.multiplication()}')
print(f'division {m.division():.2f}')
