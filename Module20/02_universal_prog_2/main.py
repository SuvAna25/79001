
def is_prime(num):
    result = [
        i_index for i_index in range(2, num // 2 + 1)if num % i_index == 0
    ]
    if not result:
        return True


def crypto(data):
    return [
        data[index] for index, value in enumerate(data)if index >= 2 and is_prime(index)
    ]


print(crypto('О Дивный Новый мир!'))
print(crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
