num_containers = int(input('Кол-во контейнеров: '))
count = 0
weight_list = []

for _ in range(num_containers):
    weight = int(input('Введите вес контейнера: '))
    if weight > 200:
        print('Ошибка: вес должен быть меньше 200.')
    weight_list.append(weight)
new_weight = int(input('Введите новый вес контейнера: '))
for i in weight_list:
    if i >= new_weight:
        count += 1
weight_list.insert(count, new_weight)
print('Номер, который получит новый контейнер: ', count + 1)




