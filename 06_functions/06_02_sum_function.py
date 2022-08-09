def mySumFunction(numberList = None) -> int:
    if numberList is None:
        return 0
    total = 0
    for number in numberList:
        total += number
    return total


print(f'Total is {mySumFunction([1, 2, 3, 4, 5])}')