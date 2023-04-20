line_1 = input('Первая строка:')
line_2 = input('Вторая строка:')
disp = 1
flag = False
for i in range(len(line_1) - 1):
    line_1 = line_1[-1] + line_1[:-1]
    if line_1 == line_2:
        flag = True
        print('Первая строка получается из второй со сдвигом', disp)
    else:
        disp += 1
if not flag:
    print('Первую строку нельзя получить из второй с помощью циклического сдвига.')

