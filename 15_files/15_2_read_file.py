try:
    my_file = open('test.txt', 'r', encoding='utf8')
    #print(my_file.readline())
    #print(my_file.readline())
    #for line in my_file:
    #    print(line)
    print(my_file.readlines())
except Exception as e:
    print(e)
finally:
    my_file.close()