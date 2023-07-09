nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]


def recursion(text):
    if text == []:
        return text
    if isinstance(text[0], list):
        return recursion(text[0] + recursion(text[1:]))
    return text[:1] + recursion(text[1:])


print('Ответ: ', recursion(nice_list))