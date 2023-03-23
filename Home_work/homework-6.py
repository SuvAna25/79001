text = []
count_text = 0
count = 0

damege = input('Введите строку: ')
text = list(damege)
text = damege.replace(':', ';')

for i in text:
    if i == ';':
        count += 1
print('Исправленная строка:', text)
print('Кол-во замен:', count)




