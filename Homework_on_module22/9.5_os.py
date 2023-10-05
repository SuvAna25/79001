import os

def find_file(cur_path, ending):
    all_paths =[]
    for i_elem in os.listdir(cur_path):
        path = os.path.join(cur_path, i_elem)
        if i_elem.endswith(ending):
            all_paths.append(os.path.abspath(path))
        elif os.path.isdir(path):
            result = find_file(path, ending)
            if result:
                all_paths.extend(result)
    return all_paths

def get_text(path_to_file):
    file = open(path_to_file, 'r', encoding='utf-8')
    result = ''
    for line in file:
        result += line
    return result


all_file = find_file('..', '.py')
file_result = open('skripts.txt', 'w', encoding='utf-8')
for file_path in all_file:
    file_result.write(get_text(file_path))
    file_result.write('\n' * 2 + '*' * 80 + '\n' * 2)
file_result.close()
