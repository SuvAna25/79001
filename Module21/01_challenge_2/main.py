def number(num):
    if num > 0:
        number(num - 1)
        print(num)


num_1 = int(input('Введите num: '))
number(num_1)


