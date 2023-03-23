films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']
films_new = []
count_f = int(input('Сколько фильмов хотите добавить?'))
for _ in range(count_f):
    print('Введите название фильма:', end=' ')
    film_list = input()
    if films.count(film_list):
        films_new.append(film_list)
    else:
        print('Ошибка: фильма ', film_list, 'у нас нет :(')
print('Ваш список любимых фильмов:', films_new)
