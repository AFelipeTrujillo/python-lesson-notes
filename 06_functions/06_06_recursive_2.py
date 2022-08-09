def desc(number):
    if number == 1:
        print(1)
        return

    print(number)
    desc(number-1)

desc(100)