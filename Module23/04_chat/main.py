while True:
    username = input('\nВведите имя:')
    print('\n1-Посмотреть текущий текст чата.'
          '\n2-Отправить сообщение.'
          '\n3-Выйти из чата.')
    action = int(input('Выберите действие: '))
    if action == 1:
        try:
            with open('history_chat.txt', 'r', encoding='utf-8') as history_file:
                for i_message in history_file:
                    print(i_message, end='')
        except FileNotFoundError:
            print('История сообщений пуста. \n')
    elif action == 2:
        try:
            with open('history_chat.txt', 'a', encoding='utf-8') as file:
                print(f'{username} Введите сообщение:')
                message = input('--> ')
                if message.strip() == '':
                    raise ValueError
                else:
                    file.write(f'{username}: {message}\n')
        except ValueError:
            print('Сообщение не может быть пустой строкой!')
    elif action == 3:
        break
    else:
        print('Ошибка! Выберите одно из доступных действий.')

