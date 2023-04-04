nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

new_list = [num_3 for num in nice_list for num_2 in num for num_3 in num_2]
print('Ответ:', new_list)