import sys

number_line = int(sys.argv[1])
argv_line = sys.argv[2]

with open('bakery.csv', 'r', encoding='utf-8') as f:
    list_strings = f.readlines()

if number_line > len(list_strings):
    print(f'Номер за пределами списка, всего срок в файле {len(list_strings)}')
else:
    with open('bakery.csv', 'w', encoding='utf-8') as f:
        list_strings[number_line-1] = argv_line + '\n'
        f.writelines(list_strings)
