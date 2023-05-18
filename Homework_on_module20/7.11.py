phone_book = {}
while True:
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    name_and_surname = (name, surname)
    if name_and_surname not in phone_book:
        phone_book[name_and_surname] = int(input('Введите номер телефона: '))
    else:
        print('Такой контакт уже существует.')
    print(phone_book)
