count_number = int(input('Кол-во чисел в списке: '))
number_list = []

for i in range(count_number):
    print('Введите', i + 1, 'число: ', end = '  ')
    number = int(input())
    number_list.append(number)

k_number = int(input('введите делитель: '))
count = 0

for num in range(count_number):
    if number_list[num] % k_number == 0:
        print('Индекс числа', number_list[num], ':', num)
        count += num

print('Сумма индексов: ', count)
