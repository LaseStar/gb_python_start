# Написать скрипт, который выводит статистику для заданной папки в виде словаря,
# в котором ключи — верхняя граница размера файла (пусть будет кратна 10),
# а значения — общее количество файлов (в том числе и в подпапках),
# размер которых не превышает этой границы, но больше предыдущей (начинаем с 0), например:
#     {
#       100: 15,
#       1000: 3,
#       10000: 7,
#       100000: 2
#     }
#
# Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
# Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.
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
    files_size[size_thr2] = len(small_sizes)

print(files_size)
