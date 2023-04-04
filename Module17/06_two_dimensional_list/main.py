word_list = 12
step = 4
new_list = [[i_num + i for i_num in range(0, word_list, step)]for i in range(1, step + 1)]
print(new_list)

#Второе решение
#word_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
#n_1 = word_list[0:12:4]
#n_2 = word_list[1:12:4]
#n_3 = word_list[2:12:4]
#n_4 = word_list[3:12:4]
#print([n_1, n_2, n_3, n_4])