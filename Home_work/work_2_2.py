count_works = int(input('Введите количество сотрудников :'))
count = 0
pay_list = []

for i in range(count_works):
    print('Введите зарплату', i + 1, 'сотрудника: ', end=' ')
    pay_for_job = int(input())
    if pay_for_job != 0:
        pay_list.append(pay_for_job)

for i in pay_list:
    count += 1

print('Осталось сотрудников:', count)
print('Зарплаты:', pay_list)

