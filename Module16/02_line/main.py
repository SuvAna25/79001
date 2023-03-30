first_class = []
second_class = []

for i in range(160, 176 + 1, 2):
    first_class.append(i)
for i in range(162, 180 + 1, 3):
    second_class.append(i)
first_class.extend(second_class)
first_class.sort()

print(first_class)