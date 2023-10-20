with open("registrations.txt", "r", encoding="utf-8") as file, \
        open("registrations_good.log", "w", encoding="utf-8") as file_good,\
        open("registrations_bad.log", "w", encoding="utf-8") as file_bad:
    for line in file:
        list = line.replace("\n", "").split(" ")
        list_info = line.replace("\n", "")
        if len(list) != 3:
            print(f"{list_info} - НЕ присутствуют все три поля: IndexError.")
            continue

        if list[0].isalpha() == False:
            print(f"{list_info} - Поле «Имя» содержит НЕ только буквы: NameError")
            file_bad.write(f"{list_info} Поле «Имя» содержит НЕ только буквы\n")
            continue

        if list[1].count('@') == 0 or list[1].count('.') == 0:
            print(f"{list_info} - Поле «Имейл» НЕ содержит @ и . (точку): SyntaxError.")
            file_bad.write(f"{list_info} Поле 'Имейл'НЕ содержит @ и .(точку)\n")
            continue

        if list[2].isdigit() == True:
            if int(list[2]) in range(10, 100):
                file_bad.write(f"{line}")
                continue
            else:
                print(f"{list_info} - Поле «Возраст» НЕ является числом от 10 до 99: ValueError.")
                file_bad.write(f"{list_info} Поле «Возраст» НЕ является числом от 10 до 99\n")
                continue
