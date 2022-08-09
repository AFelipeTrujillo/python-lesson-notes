def multiplication(*args):
    total = 1
    for arg in args:
        total *= arg
    return total

print(f'Total is {multiplication(2,3,5,6)}')