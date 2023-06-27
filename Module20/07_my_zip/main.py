text = 'abcd'
num = (10, 20, 30, 40)
def_zip = ((text[i], num[i]) for i in range(min(len(text), len(num))))
print(def_zip)
print(*def_zip, sep='\n')

def my_zip(text_zip, num_zip):
    for i in range(min(len(text_zip), len(num_zip))):
        yield text_zip[i], num_zip[i]


text = 'abcd'
num = (10, 20, 30, 40)
def_zip = my_zip(text, num)
print(def_zip)
for index, value in def_zip:
    print((index, value))

