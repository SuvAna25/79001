#input_line = set(input('Введите строку:'))
#result = set()
#for i in input_line:
#    if '0' <= i <= '9':
#        result.add(i)
#print(''.join(sorted(result)))

#Второй вариант решения
input_line = input('Введите строку:')

new_line = set(input_line)
result = new_line & set('123456789')

print(''.join(sorted(result)))
