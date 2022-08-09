def myKeys(**kwargs):
    for key, value in kwargs.items():
        print(f'key = {key}, value = {value}')


myKeys(IDE = 'Integrated Development Environment', PK = 'Primary Key')