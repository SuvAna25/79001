rollers = int(input('Количество коньков: '))
size_rollers = sorted(int(input('Размер коньков:')) for i in range(rollers))
print()
people = int(input('Количество людей: '))
size_people = sorted(int(input("Размер ноги:")) for j in range(people))
print()
count = 0

for index in size_people:
    for i in size_rollers:
        if i >= index:
            count += 1
            size_rollers.remove(i)
            break

print('Наибольшее количество людей, которые могут взять ролики:', count)


