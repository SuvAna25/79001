def programme(qustions,
              ansver = 'Неверный ввод. Пожалуйста введите да или нет',
              attempt=4):
    while True:
        bringing = input(qustions).lower()
        if bringing == 'да':
            return 1
        if bringing == 'нет':
            return 0
        attempt -= 1
        if attempt == 0:
            print('Кол-во попыток истекло')
            break
        print(ansver)
        print('Осталось попыток ', attempt)


programme('Вы действительно хотите выйти?')
programme('Удалить файл?', 'Так удалить или нет?')
programme('Записать файл?', attempt=2)