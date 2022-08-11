class Person():

    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname

    def __str__(self):
        return f'Person [{self.name}, {self.lastname}]'


class Employer(Person):

    def __init__(self, name, lastname, salary):
        super().__init__(name, lastname)
        self.salary = salary

    def __str__(self):
        return f'{super().__str__()} {self.salary}'


if __name__ == '__main__':
    e = Employer('Andy', 'Roth', 30000)
    print(e.name)