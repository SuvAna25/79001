letter_count = {}
total_letter = 0

text_file = open('text.txt', 'r').read()
for i_elem in text_file:
    if i_elem.isalpha():
        if i_elem.lower() not in letter_count:
            letter_count[i_elem.lower()] = 0
        letter_count[i_elem.lower()] += 1
        total_letter += 1


letter_freg = []
for letter, count in letter_count.items():
    freg = count / total_letter
    letter_freg.append((letter, freg))
    letter_freg.sort(key=lambda x: (-x[1], x[0]))

with open('analysis.txt', 'w') as file:
    for letter, freg in letter_freg:
        file.write(f"{letter}{freg:.3f}\n")
