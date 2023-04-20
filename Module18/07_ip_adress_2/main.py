ip_address = input('Введите IP:').split(".")
result = 'IP-адрес корректен.'
if len(ip_address) != 4:
    result = 'Адрес — это четыре числа, разделённые точками.'
else:
    for i in range(4):
        if not ip_address[i].isdigit():
            result = ip_address[i], ' — это не целое число.'
        elif not 0 < int(ip_address[i]) < 255:
            result = ip_address[i], ' превышает 255.'

print("".join(result))