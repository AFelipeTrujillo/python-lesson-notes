class Persona:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __add__(self, other):
        return f'{self.name} {other.name}'

    def __sub__(self, other):
        return self.age - other.age

p1 = Persona('Andy', 20)
p2 = Persona('Dany', 15)
print(p1 + p2)
print(p1 - p2)