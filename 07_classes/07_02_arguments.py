class Person:
    def __init__(self, name, lastname, age, *phones, **colors):
        self.name = name
        self.lastname = lastname
        self.age = age
        self.phones = phones
        self.colors = colors

    def show(self):
        print(f'{self.name} {self.lastname} {self.age} {self.phones} {self.colors}')


p = Person(name='Andy', lastname='Smith', age=33, phones = ('+134568483', '+573244556'), colors= { 'y' : 'Yellow'})
p.phone = '+134567543'
p.show()
Person.show(p)

p2 = Person('Anne', 'Rodriguez',15)
p2.show()
