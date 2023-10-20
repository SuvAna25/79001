with open('numbers.txt', 'r') as file:
    numbers = list(map(int, file.read().split()))
with open('answer.txt', 'w') as file:
    file.write(str(sum(numbers)))
