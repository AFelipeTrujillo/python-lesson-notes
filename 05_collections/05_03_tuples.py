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

numbers = (13, 1, 8, 3, 2, 5, 8)
list_of_numbers = []
for number in numbers:
    if number < 5:
        list_of_numbers.append(number)

print(f'List is {list_of_numbers}')