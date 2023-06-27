def new_contact():
    name = tuple(input('Введите имя и фамилию нового контакта (через пробел): ').title().split())
    if name not in phone_book:
        phone_book[name] = int(input('Введите номер телефона:'))
        print('Текущий словарь контактов:', phone_book)
    else:
        print('Такой человек уже есть в контактах.')
        print('Текущий словарь контактов:', phone_book)


def get_contact():
    surname = input('Введите фамилию для поиска: ').title()
    for index, value in phone_book.items():
        if surname in index:
            print(index[0], index[1], value)


phone_book = {}
while True:
    choice = int(input('\nВведите номер действия: \n'
                       '1.Добавить контакт \n'
                       '2.Найти человека '))
    if choice == 1:
        new_contact()

    elif choice == 2:
        get_contact()



