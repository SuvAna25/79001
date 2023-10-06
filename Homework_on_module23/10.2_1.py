BRUCE_WILLIS = 42
try:
    input_data = input('Введите строку: ')
    leeloo = int(input_data[4])
    result = BRUCE_WILLIS * leeloo
    print(f'- Leeloo Dallas! Multi-pass № {result}!')
except ValueError as exc:
    print(type(exc), '-невозможно преобразовать к числу')
except IndexError as exc:
    print(type(exc), '— выход за границы списка')
except Exception as exc:
    print(type(exc), '-поймано исключение')
