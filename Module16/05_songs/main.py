violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

count = 0
choice = int(input('Сколько песен выбрать? '))
for i in range(choice):
    print('Название', i + 1, '-й песни: ', end='')
    name = input()
    for i in violator_songs:
        if i[0] == name:
            count += i[1]
total = round(count, 2)
print('Общее время звучания песен — ', total)
