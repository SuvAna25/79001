import random
def get_random(n):
    return random.choices([chr(i) for i in range(ord('а'), ord('я'))], k=n)


first_letters = get_random(10)
second_letters = get_random(10)
print(first_letters, '\n', second_letters)

first_dict = dict(enumerate(first_letters))
second_dict = dict(enumerate(second_letters))
print(first_dict, '\n', second_dict)