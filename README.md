# Python Notes

![](https://i.imgur.com/3GmPd7O.png)

## Requirements 

* PyCharm Community Edition
* Python 3.10

## Lesson 1

### Hello World
```
# This is a message from Python
print("Hi there, this a hello world"
```
## Lesson 2

### Variables
```
myVariable = "Hi from Python"
print(myVariable)
myVariable = 2
print(myVariable)
```
### ID function
The output is the identity of the object passed. This is random but when running in the same program, it generates unique and same identity. 
```
print(id(x))
```
## Lesson 3

### Data types
![pyton data types](https://i.imgur.com/xnG1svc.jpg)

#### Hints and _type_ Function
```
# Int
x = 10
print(x)
print(type(x))

# String
y = "Hi there"
print(y)
print(type(y))

# String plus Hint
z : str = "bye bye"
print(z)
print(type(z))

# Float
u : float = 10.3
print(u)
print(type(u))

# Bool
flag : bool = False
print(flag)
print(type(flag))
```
#### Strings basic concatenation and spaces separator
```
myFavoriteGroup = "Pink Floyd"
category = "a psy rock band"
print("Mi favorite group is " + myFavoriteGroup + " " + category)
print("Mi favorite group is ", myFavoriteGroup, category)
```
#### Convert or cat string to integer
```
number1 = "10"
number2 = "4"
print(number1 + number2)
print(int(number1) + int(number2))
```
#### PEP 8 – Style Guide for Python Code
https://peps.python.org/pep-0008/
PEP 8, sometimes spelled PEP8 or PEP-8, is a document that provides guidelines and best practices on how to write Python code. It was written in 2001 by Guido van Rossum, Barry Warsaw, and Nick Coghlan. The primary focus of PEP 8 is to improve the readability and consistency of Python code.

#### Bool 
```
myBool = False
print(myBool)

otherBool = 2 < 4
print(otherBool)

if otherBool:
    print("the result is true")
else:
    print("the result is false")
```
### User input (input function)
```
result = input("Send something: ")
print("the result is", result)
print("END")
```
#### Convert a user input to integer
```
number1 = int(input("Number 1: "))
number2 = int(input("Number 2: "))

result = number1 + number2

print("the result is ", result)
```

## Lesson 4

### Operators

![python operators](https://i.imgur.com/Qf2TS3o.png)

#### Sum plus f-string in python
f-strings are a great new way to format strings. Not only are they more readable, more concise, and less prone to error than other ways of formatting, but they are also faster!

```
number1 = 2
number2 = 3
sum = number1 + number2
print(f'the sum is {sum}')
```
#### All operators in Python
```
number1 = 2
number2 = 3
subtraction = number1 - number2
print(f'the subtraction is {subtraction}')
multiplication = number1 * number2
print(f'the multiplication is {multiplication}')
division = number1 / number2
print(f'the division is {division}')
integer_division = number1 // number2
print(f'the division is {integer_division}')
module = number1 % number2
print(f'the module is {module}')
exp = number1 ** number2
print(f'the exponent is {exp}')
```
#### Comparison Operators
```
a = 4
b = 2

result = (a == b)
print(f'Result == {result}')
result = (a != b)
print(f'Result != {result}')
result = a > b
print(f'Result > {result}')
result = a >= b
print(f'Result >= {result}')
result = a < b
print(f'Result < {result}')
result = a <= b
print(f'Result <= {result}')
```
#### Logical Operators
```
a = True
b = False

result = a and b
print(f'Result AND {result}')
result = a or b
print(f'Result AND {result}')

result = not a
print(f'Result AND {result}')
```

#### Simplifying AND Operator
```
myVarOne = 15

if 15 <= myVarOne < 30:
    print(f'the number {myVarOne} is between 15 to 30')
```

## Lesson 5

### Python Conditional Statements

#### IF / ELSE
```
myVar = True

if myVar:
    print(f'Is True')
else:
    print(f'Is not True')
```
```
myVar = 'hi there'

if myVar == True:
    print(f'Is True')
elif myVar == False:
    print(f'Is False')
else:
    print(f'Unknown format')

```
#### Simplifying If Statements
```
myVar = True

print('This is True') if myVar else print('This is False')
```

### Python Control Statements

#### While
![while](https://i.imgur.com/OVAxks2.jpg)
```
count = 0
while count < 3:
    print(count)
    count += 1
else:
    print('END OF WHILE')
```
#### For
```
string = 'Hi there'

for word in string:
    print(word)
else:
    print("END OF FOR")
```
#### Break
```
for word in 'Holland':
    if word == 'l':
        print(f'Word found: {word}')
        break
else:
    print('END OF FOR')
```
#### Continue
```
for i in range(6):
    if i % 2 == 0:
        print(i)
        continue

for i in range(6):
    if i % 2 != 0:
        continue
    print(i)
```
## Lesson 6
### Collections
#### Lists
```
names = ['Mary', 'John', 'Lissa', 'Phill']
print(names)
print(f'Name[0]: {names[0]}')
print(f'Name[1]: {names[1]}')
print(f'Name[2]: {names[2]}')
print(f'Name[-1]: {names[-1]}') # Phill
print(f'Name[-2]: {names[-2]}') # Lissa)
```
##### Range
```
names = ['Mary', 'John', 'Lissa', 'Phill', 'Martha']
print(names[0:2])
print(names[:3])
print(names[1:])
names[1] = 'Adam'
print(names)
for name in names:
    print(name)
else:
    print('END OF FOR')
```
#### Tuples
```
fruits = ('Orange', 'Apple', 'Banana', 'Pineapple')
print(fruits)
print(f'Len {len(fruits)}')
print(fruits[0])
print(f'Inv -1 {fruits[-1]}')
print(f'Range 0-2 {fruits[0:2]}')

for fruit in fruits:
    print(fruit, end='  ')

# Set item in a tuple

fruitList = list(fruits)
fruitList[0] = 'Blackberry'
fruits = tuple(fruitList)
print(fruits)
```
#### Set
```
planets = {'Mars', 'Jupiter', 'Venus'}
print(planets)
print(len(planets))
print('Mars' in planets)
planets.add('Earth')
print(f'Set content {planets}')
planets.add('Earth')
print(f'Set content {planets}')
planets.remove('Earth')
print(f'Set content {planets}')
planets.discard('Earth')
planets.clear()
print(f'Set content {planets}')
del planets
```
#### Dictionaries
```
myDictionary = {
    'IDE': 'Integrated Development Environment',
    'OOP': 'Object Oriented Programming',
    'DBMS': 'DataBase Management System'
}

print(myDictionary)
print(len(myDictionary))
print(myDictionary['IDE'])
print(myDictionary.get('OOP'))
myDictionary['IDE'] = 'integrated development environment'
print(myDictionary)

for key, value in myDictionary.items():
    print(key, value)

for key in myDictionary.keys():
    print(key)

for value in myDictionary.values():
    print(value)

print('IDE' in myDictionary)

myDictionary['PK'] = 'Primary Key'

print(myDictionary)

myDictionary.pop('DBMS')
print(myDictionary)

myDictionary.clear()
print(myDictionary)

del myDictionary
```
## Lesson 6
### Functions
```
def myFunction():
    print('Hi there from my function')


myFunction()
```
#### Params
```
def myFunction(name):
    print(f'Hi there {name} from my function')


myFunction(name='Andy')
myFunction(name='Johanna')
```
#### Return
```
def mySumFunction(numberList = None) -> int:
    if numberList is None:
        return 0
    total = 0
    for number in numberList:
        total += number
    return total


print(f'Total is {mySumFunction([1, 2, 3, 4, 5])}')
```
#### Many Arguments
```
def myNames(*names):
    for name in names:
        print(name)


myNames('Andy', 'Johanna', 'Dany', 'Fer')
```
#### Keywords
```
def myKeys(**kwargs):
    for key, value in kwargs.items():
        print(f'key = {key}, value = {value}')


myKeys(IDE = 'Integrated Development Environment', PK = 'Primary Key')
```
#### Recursive Function
```
def factorial(number):
    if number == 1:
        return 1
    else:
        return number * factorial(number - 1)


number = 5
print(f'The factorial of {number} is {factorial(number)}')
```
## Lesson 7
### Classes and Objects
```
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
```
### Encapsulation (GET and SET)
```
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
```
## Lesson 8
### Inheritance
```
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
```
### Multi-Inheritance
```
from Shape import *
from Color import *


class Square(Shape, Color):
    def __init__(self, h, color):
        Shape.__init__(self, h,h)
        Color.__init__(self, color)

    def area(self):
        return self.h ** 2
```
### Method Resolution Order
Method Resolution Order (MRO) is an algorithm for the construction of linearization - the list of all the ancestors of a class, including the class itself, ordered from the closest to the furthest. This is the order in which methods and attributes are looked up. 
```
print(Square.mro())
```
## Lesson 10
### Static Class
#### Variables Class
```
class MyClass:
    my_var_class = 'Class var'

    def __init__(self, instance_var):
        self.instance_var = instance_var


print(MyClass.my_var_class)
obj = MyClass('Other var')
print(obj.my_var_class, obj.instance_var)

MyClass.other_class_var = 'Class var two'

obj2 = MyClass('Other var 2')
print(obj2.other_class_var)
print(obj.other_class_var)
```
#### Static Method
Use the decorator @staticmethod
```
class MyClass:
    my_var_class = 'Class var'

    def __init__(self, instance_var):
        self.instance_var = instance_var

    @staticmethod
    def static_method():
        print(MyClass.my_var_class)

MyClass.static_method()
```
#### Class and Static Method
```
class MyClass:
    my_var_class = 'Class var'

    def __init__(self, instance_var):
        self.instance_var = instance_var

    @staticmethod
    def static_method():
        print(MyClass.my_var_class)

    @classmethod
    def method_class(cls):
        print(cls.my_var_class)

    def instance_method(self):
        self.method_class()
        self.static_method()
        print(self.instance_var)

MyClass.method_class()
myObj1 = MyClass('my var')
myObj1.method_class()
myObj1.instance_method()
```
## Lesson 12
### Operator Overloading
![](https://i.imgur.com/n8d839X.png)
![](https://i.imgur.com/6WxYigZ.png)

```
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
```
## Lesson 13
### Polymorphism
**Employer Class**
```
class Employer():

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f'Employer: {self.name} Salary: {self.salary}'

    def show(self):
        return self.__str__()
```
**Manager Class**
```
from Employer import Employer


class Manager(Employer):

    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def __str__(self):
        return f'Manage {self.department} Employer {super().__str__()}'
```
**Test**
```
from Employer import Employer
from Manager import Manager

def print_details(obj):
    #print(obj)
    print(type(obj))
    print(obj.show())
    if isinstance(obj, Manager):
        print(obj.department)

e = Employer('Martha', 200000)
print_details(e)

m = Manager('Ann', 300000, 'IT')
print_details(m)
```

