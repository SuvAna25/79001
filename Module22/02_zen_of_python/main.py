import os

text_file = open('zen.txt', 'r')
data = text_file.readlines()
data.reverse()
text_file.close()
print(''.join(data))



