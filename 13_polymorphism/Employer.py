class Employer():

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f'Employer: {self.name} Salary: {self.salary}'

    def show(self):
        return self.__str__()