def summ(n):
    sum_num = 0
    while n > 0:
        num = n % 10
        sum_num = sum_num + num
        n //= 10
    return sum_num

def digits(n):
    num_count = 0
    while n > 0:
        n //= 10
        num_count += 1
    return num_count

numbers = int(input('Введите число: '))
print('Сумма чисел:', summ(numbers))
print('Количество цифр в числе:', digits(numbers))
print('Разность суммы и количества цифр:', summ(numbers) - digits(numbers))
    