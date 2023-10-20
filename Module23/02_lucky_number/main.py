import random

errors = [
    'Не повезло!',
    'Повезло, но не сильно'
]

stop = 0

with open('out_file.txt', 'w', encoding='utf-8') as file:
    while stop <= 777:
        nums = int(input('Введите число: '))
        stop += nums
        if 13 == random.randint(1, 13):
            raise Exception(random.choice(errors))
        if stop == 777:
            print('Вы успешно выполнили условие!')
            break
        print(nums, file=file)
