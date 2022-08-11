class Vehicle:

    def __init__(self, color, number_of_wheels):
        self.color = color
        self.number_of_wheels = number_of_wheels

    def __str__(self):
        return f'Vehicle[{self.color}, {self.number_of_wheels}]'


class Car(Vehicle):

    def __init__(self, color, number_of_wheels, speed):
        super().__init__(color, number_of_wheels)
        self.speed = speed

    def __str__(self):
        return f'Car[{self.speed}] Vehicle[{self.color}, {self.number_of_wheels}]'


class Bike(Vehicle):

    def __init__(self, color, number_of_wheels, type):
        super().__init__(color, number_of_wheels)
        self.type = type

    def __str__(self):
        return f'Bike[{self.type}] Vehicle[{self.color}, {self.number_of_wheels}]'
