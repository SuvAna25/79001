test = False
letters = 0
num = 0

while True:
    password = input('Придумайте пароль:')
    if len(password) > 8:
        test = True
    for i in range(len(password)):
        if password[i].istitle():
            letters += 1
    for i in range(len(password)):
        if password[i].isdigit():
            num += 1
    if test and letters >= 1 and num >= 3:
        print('Это надёжный пароль.')
        break
    else:
        print('Пароль ненадёжный. Попробуйте ещё раз.')







