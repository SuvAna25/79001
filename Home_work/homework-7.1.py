text =input('Введите строку: ')
sym_num = int(input('Номер символа: ')) -1
letters = list(text)
count = 0

if sym_num > 0:
    print('Символ слева: ', letters[sym_num - 1])
    if letters[sym_num - 1] == letters[sym_num]:
        count += 1
if sym_num < len(letters) - 1:
    print('Символ справа: ', letters[sym_num + 1])
    if letters[sym_num + 1] == letters[sym_num]:
        count += 1
if count == 0:
    print('Таких же символов нет.')
elif count == 1:
    print('Есть ровно один такой же символ.')
else:
    print('Есть 2 таких же символа.')
