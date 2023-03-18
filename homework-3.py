employees = int(input('Кол-во сотрудников в офисе: '))
num_employees = []
for _ in range(employees):
    num = int(input('ID сотрудника: '))
    num_employees.append(num)
numbers = int(input('Какой ID ищем? '))

search = False
for i in num_employees:
    if i == numbers:
        search = True
if search:
    print('Сотрудник работает!')
else:
    print('Сотрудник не работает!')
