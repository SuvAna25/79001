import os

path_to = input('Путь: ')
if os.path.isdir(path_to):
    print('Это папка!')
elif os.path.isfile(path_to):
    print('Это файл!')
    print('Размер файла:', os.path.getsize(path_to), 'байт')
else:
    print('Указанного пути не существует')

