from Employer import Employer


class Manager(Employer):

    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def __str__(self):
        return f'Manage {self.department} Employer {super().__str__()}'
