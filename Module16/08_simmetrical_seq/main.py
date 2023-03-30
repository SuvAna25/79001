numbers = int(input('Количество чисел: '))
list_num = []
for _ in range(numbers):
    list_num.append(int(input('Число:')))
print('Последовательность: ', list_num)
num_count = 0
while list_num != list_num[::-1]:
    list_num.insert((numbers),list_num[num_count])
    num_count += 1
print('Нужно приписать чисел:', num_count)
print('Сами числа: ', list_num[:num_count][::-1])

