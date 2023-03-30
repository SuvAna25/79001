guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
    print('Сейчас на вечеринке ', len(guests), 'человек:', guests)
    question = input('Гость пришёл или ушёл? ')

    if question == 'пришёл':
        name = input('Имя гостя: ')
        if len(guests) >= 6:
            print('Прости,', name, ', но мест нет.')
            print()
        else:
            print('Привет,', name, '!')
            print()
            guests.append(name)

    elif question == 'ушёл':
        name = input('Имя гостя: ')
        print('Пока,', name, '!')
        guests.remove(name)
        print()
    elif question == 'Пора спать' or 'пора спать':
        print('Вечеринка закончилась, все легли спать.')
        break