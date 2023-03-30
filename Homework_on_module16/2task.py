line = input('Введите строку: ')
symbol = input('Введите дополнительный символ:')

doubled_list = [i * 2 for i in line]
gluing_symbols = [(i * 2) + symbol for i in line]

print('Список удвоенных символов:', doubled_list)
print('Склейка с дополнительным символом:', gluing_symbols)