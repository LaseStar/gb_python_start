# Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
# Написать скрипт, который собирает все шаблоны в одну папку templates, например:
# |--my_project
#    ...
#    |--templates
#    |   |--mainapp
#    |   |  |--base.html
#    |   |  |--index.html
#    |   |--authapp
#    |      |--base.html
#    |      |--index.html

# Примечание: исходные файлы необходимо оставить;
# обратите внимание, что html-файлы расположены
# в родительских папках (они играют роль пространств имён);
# предусмотреть возможные исключительные ситуации; это реальная задача,
# которая решена, например, во фреймворке django.
import os
import shutil


# для содание папок
def make_dir(name, folder=''):
    dir_path = os.path.join(folder, name)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    return


# Процедура для копирования файлов
def my_copy_file(file_folder, new_folder):
    # Получить имя файла по текущему пути и вернуть список
    file_names = os.listdir(file_folder)
    for file in file_names:
        # Добавить имя файла к текущему пути к файлу
        new_dir = f'{file_folder}\\{file}'
        # Если это файл
        if os.path.isfile(new_dir):
            new_file = f'{new_folder}\\{file}'
            shutil.copyfile(new_dir, new_file)
        else:
            # Если это не файл, рекурсивно укажите путь к этой папке
            my_copy_file(new_dir, new_folder)
    return


# Создаем папку templates в корне проекта
dir_templates = 'templates'
dir_main = 'my_project'
make_dir(dir_templates, dir_main)
main_folder = f'{dir_main}\\{dir_templates}'

for root, dirs, files in os.walk('my_project'):
    if 'templates' in root and dirs and not main_folder in root:
        for dir in dirs:
            make_dir(dir, main_folder)
            my_copy_file(f'{root}\\{dir}', f'{main_folder}\\{dir}')
