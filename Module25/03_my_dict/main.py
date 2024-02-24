class MyDict(dict):
    def get(self, key, default=0):
        return super().get(key, default)


new_dict = MyDict()
new_dict['Вася'] = 1
new_dict['Петя'] = 2
new_dict['Коля'] = 3
print(new_dict)
print(new_dict.get('Аня'))
