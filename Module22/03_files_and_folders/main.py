import os


def count_file(path):
    size = 0
    file = 0
    dirs = 0
    for dirapth, dirnames, filenames in os.walk(path):
        for i in filenames:
            j = os.path.join(dirapth, i)
            size += os.path.getsize(j)
            file += 1
        dirs += len(dirnames)
    return file, dirs, size


path = input('Введите путь до каталога: ')
(file, dirs, size) = count_file(path)

print('Размер каталога (в Кб):', size / 1024)
print('Кол-во подкаталогов: ', dirs)
print('Кол-во файдлов: ', file)
