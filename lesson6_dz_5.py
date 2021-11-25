# ** (вместо 4) Решить задачу 4 и реализовать интерфейс командной строки,
# чтобы можно было задать путь к обоим исходным файлам и путь к выходному файлу со словарём.
# Проверить работу скрипта для случая, когда все файлы находятся в разных папках.

import sys
from itertools import zip_longest
import json

users_path = sys.argv[1]
hobby_path = sys.argv[2]
result_path = sys.argv[3]

with open(users_path, 'r', encoding='utf-8') as f1, open(hobby_path, 'r', encoding='utf-8') as f2:
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
# Потом легче по клбчу обращаться
for idx, item in users_hobby.items():
    user = idx.split(' ')
    user.append(item)
    users_hobby[idx] = user

with open(result_path, 'w') as f:
    json.dump(users_hobby, f)

with open(result_path) as f:
    data = json.load(f)
print(data)
