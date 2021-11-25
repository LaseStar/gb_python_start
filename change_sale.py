import sys

number_line = int(sys.argv[1])
argv_line = sys.argv[2]

# Тут без выполнения одного из условий
# Но код проще )))
with open('bakery.csv', 'r', encoding='utf-8') as f:
    list_strings = f.readlines()

if number_line > len(list_strings):
    print(f'Номер за пределами списка, всего срок в файле {len(list_strings)}')
else:
    with open('bakery.csv', 'w', encoding='utf-8') as f:
        list_strings[number_line-1] = argv_line + '\n'
        f.writelines(list_strings)

# Сохранил и разобрал
edit_idx, new_val = sys.argv[1:]
with open('bakery.csv', 'r+') as f:
    tmp_file = open('bakery.tmp', 'w+')
    change = False
    for idx, item in enumerate(f, 1):
        if idx == int(number_line):
            tmp_file.write(f'{argv_line}\n')
            change = True
        else:
            tmp_file.write(item)
    if not change:
        exit('ERROR!!!')

    tmp_file.seek(0)

    f.truncate(0)
    for line in tmp_file:
        f.write(line)
    tmp_file.close()
