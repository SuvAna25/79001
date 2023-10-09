fileinput = None
try:
    fileinput = open('file.txt', 'w', encoding='utf-8')
    text = int(input('Введите строку:'))
    fileinput.write(str(text))
except (FileNotFoundError, PermissionError) as exc:
    print(type(exc), exc)
except ValueError as exc:
    print(type(exc), exc)
except Exception as exc:
    print(type(exc), exc)
else:
    print('Запись прошла без ошибок')
finally:
    fileinput.close()
    print(fileinput.closed)



