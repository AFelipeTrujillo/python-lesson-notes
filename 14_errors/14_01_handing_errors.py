result = None
a = '10'
b = 0
try:
    result = a / b
except ZeroDivisionError as e:
    print(f'An error is happened: {e}')
except TypeError as e:
    print(f'An type error is happened: {e}')
except Exception as e:
    print(f'An type error is happened: {e}')

print(f'Result: {result}')
print('Continue...')

