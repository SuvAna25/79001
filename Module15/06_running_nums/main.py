original_list = [1, 2, 3, 4, 5]
disp = 1

print('Сдвиг:', disp)
print('Изначальный список: ', original_list)

while disp <=5:
    last_list = original_list[-disp:] + original_list[:-disp]
    print('Сдвинутый список: ', last_list)
    disp += 1
