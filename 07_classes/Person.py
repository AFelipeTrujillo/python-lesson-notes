class Person:
    def __init__(self, name, lastname, age):
        self._name = name
        self._lastname = lastname
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def lastname(self):
        return self._lastname

    @lastname.setter
    def lastname(self, lastname):
        self._lastname = lastname

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def show(self):
        print(f'{self.name} {self.lastname} {self.age}')

    def __del__(self):
        print(f'Person to delete {self._name} {self._lastname}')


if __name__ == '__main__':
    p = Person(name='Andy', lastname='Smith', age=33)
    print(p.name)
    p.name = 'John'
    p.lastname = 'Doe'
    p.show()
