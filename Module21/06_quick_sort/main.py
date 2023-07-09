import random

numbers = [4, 9, 2, 7, 5]


def sorting(num):
    if len(num) <= 1:
        return num
    else:
        number = random.choice(num)
        number_1 = [elem for elem in num if elem < number]
        number_2 = [number] * num.count(number)
        number_3 = [elem for elem in num if elem > number]
        return sorted(number_1) + number_2 + sorted(number_3)


print(sorting(numbers))