
try:
    my_file = open('test.txt', 'w', encoding='utf8')
    my_file.write('Add info\n')
    my_file.write('áéíó\n')
    my_file.write('bye')
except Exception as e:
    print(e)
finally:
    my_file.close()
    print('File close')