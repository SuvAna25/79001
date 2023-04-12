# Напишите программу, которая получает на вход 4 числа и выводит
# на экран IP-адрес. Используйте переменную ip_address в качестве
# шаблона. Обеспечьте контроль ввода.

ip_address = '{0}.{1}.{2}.{3}'
count = 0
new_num = []
while count < 4:
    num = int(input('Введите число:'))
    if 0 <= num <= 255:
        new_num.append(num)
        count += 1
print(ip_address.format(new_num[0], new_num[1], new_num[2], new_num[3]))



