first_man = [1, 5, 3]
second_man = [1, 5, 1, 5]
third_man = [1, 3, 1, 5, 3, 3]

first_man.extend(second_man)
count_5 = first_man.count(5)
for i in first_man:
    if i == 5:
        first_man.remove(5)
first_man.extend(third_man)
count_3 = first_man.count(3)

print('Количество цифр 5 при первом объединении: ', count_5)
print('Количество цифр 3 при втором объединении: ', count_3)
print('Итоговый список: ', first_man)


