
count_line = 0

try:
    palindrome_file = open('palindrome.txt', 'r', encoding='utf-8').read()
    for i_line in palindrome_file:
        clear_line = i_line.rstrip()
        if clear_line.isalpha() and clear_line == clear_line[::-1]:
            count_line += 1
        else:
            raise ValueError('Строка не полностью состоит из букв!')

except ValueError as exc:
    errors_file = open('errore.log', 'w', encoding='utf-8').write(str(exc))


print(count_line)
