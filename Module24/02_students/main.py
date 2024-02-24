class Student:
    def __init__(self, name, group, grade):
        self.name = name
        self.group = group
        self.grade = grade

    def score(self):
        return (sum(self.grade) / len(self.grade))

    def __str__(self):
        return (self.name)


students = []
for i in range(5):
    print(f'студент {i + 1}:')
    name = input('Имя, Фамилия: ')
    group = int(input('Номер группы: '))
    grade = list(map(int, input('Оценки через пробел: ').split()))
    students.append(Student(name, group, grade))

stud_sorted = sorted(students, key=lambda student: student.score())
print(*stud_sorted, sep='\n')
