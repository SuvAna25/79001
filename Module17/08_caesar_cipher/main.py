def code(text_1, step_1):
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    result = ''.join([(alphabet[(alphabet.index(letter) + step_1) % 33]
                      if letter in alphabet else letter) for letter in text_1])
    return result

text = input('Введите сообщение:')
step = int(input('Введите сдвиг:'))

print('Зашифрованное сообщение:', code(text, step))

