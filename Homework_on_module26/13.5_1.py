def counter():
    num = 0
    while True:
        num += 1
        yield num


def get_prime_num(num):
    prime_num = []
    for number in range(2, num + 1):
        for prime in prime_num:
            if number % prime == 0:
                break
        else:
            prime_num.append(number)
            yield number


for i in get_prime_num(50):
    print(i, end="\t")
print()