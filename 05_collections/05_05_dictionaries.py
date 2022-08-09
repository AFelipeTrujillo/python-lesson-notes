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