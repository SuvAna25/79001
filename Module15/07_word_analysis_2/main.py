word_list = []
word = input('Введите слово: ')
for i in word:
    word_list.append(i)
revers_word_list = word_list[::-1]
if word_list == revers_word_list:
    print('Слово является палиндромом')
else:
    print('Слово не является палиндромом')

