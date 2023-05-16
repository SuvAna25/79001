text = input('Введите строку:')
text_palindrom = set()
for i in text:
    if i in text_palindrom:
        text_palindrom.remove(i)
    else:
        text_palindrom.add(i)
print(('Можно','Нельзя')[len(text_palindrom)>1], 'сделать полиндром')