way = input('Путь к файлу: ')
dick = input('На каком диске должен лежать файл: ')
widening = input('Требуемое расширение файла: ')
if way.startswith(dick) and way.endswith(widening):
    print('Путь корректен!')
else:
    print('Путь не корректен!')
