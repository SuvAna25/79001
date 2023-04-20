text = input('Введите строку:')
count = 1
result = ''
for i in range(len(text)):
    if i == len(text) - 1:
        result += text[i] + str(count)
    elif text[i] == text[i + 1]:
        count += 1
    else:
        result += text[i] + str(count)
        count = 1
print('Закодированная строка:', result)
