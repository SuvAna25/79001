while True:
    template = input('Введите шаблон поздравления, '
                 'в шаблоне должна быть конструкция '
                 '{name} и {age}: ')
    if '{name}' in template and '{age}' in template:
        break
    print('Ошибка, отсутсвует одна или две конструкции.')
name_list = input('Список людей через запятую: ').split(', ')
age_str = input('Введите возраст через пробел: ')
ages = [int(i_number) for i_number in age_str.split()]
for i_man in range(len(name_list)):
    print(template.format(name = name_list[i_man], age = ages[i_man]))

people = [
' '.join([name_list[i_man], str(ages[i_man])])
    for i_man in range(len(name_list))
]

people_str = ', '.join(people)

print(people_str)