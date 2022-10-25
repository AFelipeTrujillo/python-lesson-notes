from SameNumbersException import SameNumbersException

result = None
a = 10
b = 10
try:
    if a == b:
        raise SameNumbersException('Numbers are the same')
    result = a / b
except ZeroDivisionError as e:
    print(f'An error is happened: {e}')
except TypeError as e:
    print(f'An type error is happened: {e}')
except SameNumbersException as e:
    print(f'Same Numbers: {e}')
except Exception as e:
    print(f'An type error is happened: {e}')
else:
    print('NO EXCEPT')
finally:
    print('EXCEPT ENDS')

print(f'Result: {result}')
print('Continue...')

