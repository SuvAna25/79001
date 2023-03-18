first_date = int(input('Введите первый год: '))
second_date = int(input('Введите второй год: '))
print('Годы от', first_date, 'до', second_date, 'с тремя одинаковыми цифрами:')

for num in range(first_date, second_date + 1):
    number_4 = num % 10
    num //= 10
    number_3 = num % 10
    num //= 10
    number_2 = num % 10
    num //= 10
    number_1 = num
    if ((number_4 == number_3) and (number_3 == number_2)) or \
            ((number_4 == number_3) and (number_3 == number_1)) or \
            ((number_1 == number_2) and (number_1 == number_4)) or \
            ((number_1 == number_2) and (number_1 == number_3)):
        print(number_1 * 1000 + number_2 * 100 + number_3 * 10 + number_4)
