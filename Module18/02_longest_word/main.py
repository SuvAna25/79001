text = input('Введите строку:').replace('.', ' ')
word_text = max(text.split(), key=len)

if len(word_text) == 1:
    symbol = 'символ.'
elif len(word_text) < 5:
    symbol = 'символа.'
else:
    symbol = 'символов.'

print('Самое длинное слово:', f'"{word_text}".')
print('Длина этого слова:', len(word_text), f'{symbol}')
