def existe(i_film, film_list):
    for movie in film_list:
        if movie == i_film:
            return True
    return False

def revision(film, films_list):
    for i_films in films_list:
        if i_films == film:
            return True
    return False

films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
    'Леон', 'Богемская рапсодия', 'Город грехов',
    'Мементо', 'Отступники', 'Деревня',
    'Проклятый остров', 'Начало', 'Матрица'
]
top_films = []
while True:

    print('\nВаш текущий топ фильмов: ', top_films)
    name_films = input('Название фильма: ')
    if existe(name_films, films):
        print('Команды: добавить, вставить, удалить', end=' ')
        command = input()
        if command == 'добавить':
            if revision(name_films, top_films):
                print('Этот фильм уже есть в вашем списке')
            else:
                top_films.append(name_films)
        if command == 'вставить':
            if revision(name_films, top_films):
                print('Этот фильм уже есть в вашем списке')
            else:
                num = int(input('На какое место? '))
                top_films.insert(num - 1, name_films)
        if command == 'удалить':
            top_films.remove(name_films)

    else:
        print('Такого фильма нет.')
