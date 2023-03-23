list_name = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений',
             'Женя', 'Захар']
list_name_new = []
for i in range(len(list_name)):
    if i % 2 != 1:
        list_name_new.append(list_name[i])
print(list_name_new)

