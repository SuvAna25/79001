import os

numbers_file = open('numbers.txt', 'r', encoding='utf-8')
count_num = 0
for i_line in numbers_file:
    clear_line = i_line.rstrip()
    if clear_line:
        count_num += int(i_line)
numbers_file.close()

count_file = open('answer.txt', 'w', encoding='utf-8')
count_file.write(str(count_num))
count_file.close()