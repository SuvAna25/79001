numbers = int(input('Введите число: '))
i_numbers = []
for i in range(1, numbers, 2):
    i_numbers.append(i)
print('Список из нечетных чисел от одного до N: ', i_numbers)
