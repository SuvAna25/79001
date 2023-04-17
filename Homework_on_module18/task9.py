text = input('Введите строку: ')
lowers = len([letter for letter in text if letter.islower()])
uppers = len([letter for letter in text if letter.isupper()])
if lowers > uppers:
    print('Результат: ', text.lower())
else:
    print('Результат: ', text.upper())