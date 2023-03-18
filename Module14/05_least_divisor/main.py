
def gcd(number):
    gcd = 1
    for num in range(1, number + 1):
        if number % num == 0:
            gcd = num
        if gcd > 1:
            break
    return gcd


number = int(input('Введите число '))
go_gcd = gcd(number)
print('Наименьший делитель,u отличный от 1: ',go_gcd )
