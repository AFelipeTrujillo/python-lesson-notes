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