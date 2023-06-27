students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def function(students_dict):
    interests_dict = []
    surname_list = ''
    for i in students_dict:
        interests_dict += (students_dict[i]['interests'])
        surname_list += (students_dict[i]['surname'])
    count = 0
    for _ in surname_list:
        count += 1
    return interests_dict, count


age_id_list = []
for i_id, info in students.items():
    for i_point, i_data in info.items():
        if i_point == 'age':
            age_id_tuple = (i_id, i_data)
            age_id_list.append(age_id_tuple)


my_list = function(students)[0]
count_surname = function(students)[1]
print(f'Список пар «ID студента — возраст»: {age_id_list}\n',
      f'Полный список интересов всех студентов: {my_list}\n',
      f'Общая длина всех фамилий студентов: {count_surname}')
