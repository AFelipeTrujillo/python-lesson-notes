my_file = open('test.txt', 'r', encoding='utf8')
my_file_2 = open('copy.txt', 'a', encoding='utf8')
my_file_2.write(my_file.read())
my_file.close()
my_file_2.close()