def factorial(num):
    if num == 1:
        return num
    fact = factorial(num - 1)
    return num * fact


num_fact = factorial(5)
print(num_fact)