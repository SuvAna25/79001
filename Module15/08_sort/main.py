num_list = [1, 4, -3, 0, 10]
len_num = len(num_list)

print('Изначальный список: ', num_list)

for i in range(1, len_num):
    for j in range(len_num - 1, i - 1, -1):
        if num_list[j - 1] > num_list[j]:
            num_list[j - 1], num_list[j] = num_list[j], num_list[j - 1]

print('Отсортированный список: ', num_list)
