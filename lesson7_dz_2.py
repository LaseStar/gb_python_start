# *(вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта со следующей структурой:
import os


# для содание папок
def make_dir(name, folder=''):
    dir_path = os.path.join(folder, name)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


#  для создания файлов
def make_file(name):
    with open(name, 'tw') as f:
        pass


# Для получение строки по номеру из файла
def read_line_from_file(line_number):
    with open(file_name, 'r') as f:
        for line_no, line in enumerate(f):
            if line_no == line_number:
                return line


def create_yaml(num, folder=''):
    for _ in range(num, len_file):
        line = read_line_from_file(_).strip("\n")

        if not folder:
            folder = line.replace('|--', '')
            make_dir(folder)
            dict_dir.setdefault(0, folder)
            return create_yaml(num+1, folder)
        elif not '.' in line:
            _num = line.find('|--')
            name_dir = line[_num+3:]
            dict_dir.setdefault(int(_num/3), name_dir)
            dict_dir[int(_num/3)] = name_dir
            # Определяем folder
            i = 1
            folder_ = ''
            while i < _num/3:
                folder_ = folder_ + f'\\{dict_dir[i]}'
                i += 1
            make_dir(name_dir, folder+folder_)
            return create_yaml(num + 1, folder)
        else:
            _num = line.find('|--')
            name_file = line[_num + 3:]
            # Определяем folder
            i = 1
            folder_ = ''
            while i < _num / 3:
                folder_ = folder_ + f'\\{dict_dir[i]}'
                i += 1
            make_file(folder+folder_+f'\\{name_file}')
            return create_yaml(num + 1, folder)


# Тут узнаем длину файла
file_name = 'config.yaml'
dict_dir = {}

with open(file_name) as f:
    list_strings = f.readlines()
len_file = len(list_strings)

create_yaml(0)