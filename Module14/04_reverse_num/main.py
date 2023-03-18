def num_back(number):
    parts = str(number).split('.')
    parts[0] = ''.join(reversed(list(str(parts[0]))))
    parts[1] = ''.join(reversed(list(str(parts[1]))))
    return float(parts[0] + '.' + parts[1])

first = (input('Введите первое число: '))
second = (input('Введите второе число: '))

first_back = num_back(first)
second_back = num_back(second)

print('Первое число наоборот: ', first_back)
print('Второе число наоборот: ', second_back)
print('Сумма: ', first_back + second_back)


