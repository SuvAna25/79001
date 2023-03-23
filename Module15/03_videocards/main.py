quantity = int(input('Количество видеокарт: '))
old_list = []
new_list = []
for i in range(quantity):
    print('Видеокарта', i +1, ': ', end=' ')
    vi_card = int(input(''))
    old_list.append(vi_card)
print('Старый список видеокарт: ', old_list)
max_card = max(old_list)
for id in old_list:
    if id != max_card:
        new_list.append(id)

print('Новый список видеокарт: ', new_list)


