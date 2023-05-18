def get_index(text_index, symbol):
    return [str(index) for index, letter in enumerate(text_index) if letter == symbol]


text = input('Строка: ')
print('Ответ', " ".join(get_index(text, '~')))
