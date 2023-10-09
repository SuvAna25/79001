text_count = 0
line_count = 0
try:
    people_file = open('people.txt', 'r')
    for i_line in people_file:
        length = len(i_line)
        line_count += 1
        if i_line.endswith('\n'):
            length -= 1
        if length < 3:
            raise BaseException('Длина {} строки меньше 3 символов'.format(line_count))
        text_count += length
    people_file.close()
except FileNotFoundError:
    print('Файл не найден')
finally:
    print('Найдена сумма символов:', text_count)
