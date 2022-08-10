class Person:
    def __init__(self, name, lastname, age):
        self._name = name
        self.lastname = lastname
        self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def show(self):
        print(f'{self.name} {self.lastname} {self.age}')


p = Person(name='Andy', lastname='Smith', age=33)
print(p.name)
p.name = 'John'
print(p.name)


