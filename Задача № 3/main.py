import os

def all_text_files(files):
    result = []
    for file in files:
        if file.endswith('.txt'):
            with open(file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                result.append([file, str(len(lines)),lines])
    result = sorted(result, key=lambda x: x[1])
    for item in result:
        with open('new_file.txt', 'a', encoding='utf-8') as f:
            f.write('\n' + item[0] + '\n')
            f.write(item[1] + '\n')
            for line in item[2]:
                f.write(f'{line}')

all_text_files(os.listdir())