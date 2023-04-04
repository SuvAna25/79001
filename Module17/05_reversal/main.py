word = input('Введите строку:')
revers = word[word.find('h') + 1:word.rfind('h')]
word = revers[::-1]

print('Развёрнутая последовательность между первым и последним h:', word)
