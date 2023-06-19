def text(string):

    if type(string) == dict:
        print('Тип данных: dict (словарь)')
        print('Изменяемый (mutable)')
    elif type(string) == str:
        print('Тип данных: str (строка)')
        print('Неизменяемый (immutable)')
    print('ID обьекта: ', id(string))


print(text('привет'))
print(text({'a': 10, 'b': 20}))