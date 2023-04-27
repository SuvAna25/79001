text = set(input('Введите строку: '))
symbol = set('.,;:!?')
print('Количество знаков пунктуации:', len(text.intersection(symbol)))
