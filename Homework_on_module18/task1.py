name = input('Имя:')
numbers = int(input('Номер заказа: '))

order = 'Здравствуйте, {0}! Ваш номер заказа: {1}. Приятного дня!'.format(
    name,
    numbers
)

print(order)