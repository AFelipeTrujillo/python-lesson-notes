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