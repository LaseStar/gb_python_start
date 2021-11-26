# *(вместо 4) Написать скрипт, который выводит статистику для заданной папки в виде словаря,
# в котором ключи те же, а значения — кортежи вида (<files_quantity>, [<files_extensions_list>]), например:
#     {
#       100: (15, ['txt']),
#       1000: (3, ['py', 'txt']),
#       10000: (7, ['html', 'css']),
#       100000: (2, ['png', 'jpg'])
#     }
#
# Сохраните результаты в файл <folder_name>_summary.json в той же папке, где запустили скрипт.
import os


dir_main = 'some_data'
# Узнаем максимум для словаря
sizes = [len(str(item.stat().st_size)) for item in os.scandir(dir_main)]
max_size = max(sizes)

# создаем словарь
files_size = {}
for i in range(0, max_size+1):
    size_thr1 = 10**(i-1)
    size_thr2 = 10**i
    small_sizes = [item.name for item in os.scandir(dir_main) if size_thr1 < item.stat().st_size < size_thr2]
    suffixes = set([os.path.splitext(f)[1] for f in small_sizes])
    files_size[size_thr2] = (len(small_sizes), list(suffixes))

print(files_size)
