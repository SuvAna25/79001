people = int(input('Количество человек:'))
out = int(input('Какое число в считалке? '))
result = 1

print('Значит, выбывает каждый', out, '-й человек')
people_list = list(range(1, people + 1))

for _ in range(len(people_list) - 1):
    print('\nТекущий круг людей: ', people_list)
    print('Начало счёта с номера ', people_list[(result - 1) % len(people_list)])

    people_index = (out + result - 1) % len(people_list)
    print('Выбывает человек под номером', people_list[people_index - 1])
    p_index = people_list[people_index - 1]
    result = people_list.index(p_index) + 1
    people_list.remove(p_index)
print('\nОстался человек под номером ', people_list[0])
print()