first_dam = []
second_dam = []
bad_thing = 0

num_dam = int(input('Кол-во пакетов:'))

for i in range(num_dam):
    print('\nПакет номер', i + 1)
    for index in range(4):
        print(index + 1, 'бит:', end=' ')
        number = int(input())
        first_dam.append(number)
    if first_dam.count(-1) <= 1:
        second_dam.extend(first_dam)
    else:
        print('Много ошибок в пакете ')
        bad_thing += 1
    first_dam = []

print('Полученное сообщение:', second_dam)
print('Кол-во ошибок в сообщении:', second_dam.count(-1))
print('Кол-во потерянных пакетов: ',bad_thing )