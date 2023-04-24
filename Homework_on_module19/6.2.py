#Студент
#Пользователь вводит фамилию, имя студента, город проживания,
#вуз, в котором он учится, и все его оценки. Всё вводится в одну
#строку через пробел. Напишите программу, которая по этой информации
#составит словарь и выведет его на экран.

student_new = input('Введите информацию о студенте через пробел\n'
                '(имя, фамилия, город, место учёбы, оценки): ')
student_info = student_new.split()
student = dict()
student['Имя'] = student_info[0]
student['Фамилия'] = student_info[1]
student['Город'] = student_info[2]
student['Место учебы'] = student_info[3]
student['Оценки'] = []
for i in student_info[4:]:
    student['Оценки'].append(int(i))
for info in student:
    print(info, '-', student[info])

