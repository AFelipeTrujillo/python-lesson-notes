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
