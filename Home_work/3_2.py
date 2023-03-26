first_word = input("Первое сообщение: ")
second_word = input("Первое сообщение: ")

first_count = first_word.count("!") + first_word.count("?")
second_count = second_word.count("!") + second_word.count("?")
if first_count < second_count:
    print('Третье сообщение: ', second_word + first_word)
elif first_count > second_count:
    print('Третье сообщение: ', first_word + second_word)
else:
    print('Ой')
