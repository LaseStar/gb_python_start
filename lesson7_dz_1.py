# Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
# |--my_project
#    |--settings
#    |--mainapp
#    |--adminapp
#    |--authapp

import os


def make_dir(name, folder=''):
    dir_path = os.path.join(folder, name)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    else:
        print(f'{dir_path} - уже существует')


if __name__ == '__main__':
    main_dir = 'my_project'
    user_dir = ('settings', 'mainapp', 'adminapp', 'authapp')
    make_dir(main_dir)
    for item in user_dir:
        make_dir(item, main_dir)
