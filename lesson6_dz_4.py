# * (вместо 3) Решить задачу 3 для ситуации, когда объём данных в файлах превышает объём ОЗУ
# (разумеется, не нужно реально создавать такие большие файлы, это просто задел на будущее проекта).
# Также реализовать парсинг данных из файлов — получить отдельно фамилию, имя и отчество для пользователей
# и название каждого хобби: преобразовать в какой-нибудь контейнерный тип (список, кортеж, множество, словарь).
# Обосновать выбор типа. Подумать, какие могут возникнуть проблемы при парсинге.
# В словаре должны храниться данные, полученные в результате парсинга.
import sys
from itertools import zip_longest
import json

with open('users.csv', 'r', encoding='utf-8') as f1, open('hobby.csv', 'r', encoding='utf-8') as f2:
    line1 = [k.strip("\n").strip().replace(',', ' ') for k in f1.readlines()]
    line2 = [k.strip("\n").strip() for k in f2.readlines()]

    if len(line1) < len(line2):
        sys.exit(1)

    users_hobby = dict(zip_longest(line1, line2))

# Работаем со словарем
# Делаем внутри словаря список
# 0 - фамилия
# 1 - имя
# 2 - отчество
# 3 - хобби
# Потом легче по ключу обращаться
for idx, item in users_hobby.items():
    user = idx.split(' ')
    user.append(item)
    users_hobby[idx] = user

with open('users_hobby.json', 'w') as f:
    json.dump(users_hobby, f)

with open('users_hobby.json') as f:
    data = json.load(f)
print(data)
