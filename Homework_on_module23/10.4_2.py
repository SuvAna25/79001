
def check_palindrome(word):
    return word == word[::-1]


with open('word.txt', 'r', encoding='utf8') as file, open('errors.log', 'w', encoding='utf8') as log_file:
    count = 0

    for line in file:
        try:
            clear_line = line.rstrip()
            if clear_line.isalpha():
                count += check_palindrome(clear_line)
            else:
                raise ValueError("строка не полностью состоит из букв!")
        except ValueError as exc:
            log_file.write(str(exc))

    print(count)
