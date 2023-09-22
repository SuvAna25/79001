import os

def look_file(full_path, file_name):
    print('Ищем в:'), os.path.join(os.path.abspath(full_path))
    for i in os.listdir(full_path):
        path = os.path.join(full_path, i)
        print('Путь', path)
        if file_name == i:
            print(os.path.abspath(path))
        elif os.path.isdir(path):
            result = look_file(path, file_name)
            if result:
                break
    else:
        result = None
    return result
look_file('C:/Users/Suver/PycharmProjects', 'lesson2.py')
