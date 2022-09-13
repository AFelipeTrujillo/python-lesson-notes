class Persona:
    count_people = 0

    @classmethod
    def add_person(cls):
        cls.count_people += 1
        return cls.count_people

    def __init__(self, name, age):
        self.id = Persona.add_person()
        self.name = name
        self.age = age

    def __str__(self):
        return f'Persona {self.id} {self.name} {self.age}'


person1 = Persona('john', 10)
print(person1)
person2 = Persona('Mary', 25)
print(person2)
person3 = Persona('Charles', 25)
print(person3)

print(f'Count {Persona.count_people}')