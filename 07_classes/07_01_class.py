class Person:
    my_attribute = ''

    def __init__(self):
        self.name = 'John'
        self.lastname = 'Doe'
        self.age = 28
        pass

    def __str__(self):
        pass

    def __repr__(self):
        pass

person1 = Person()
print(person1.name)
print(person1.lastname)
print(person1.age)