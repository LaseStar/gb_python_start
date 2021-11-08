# Создать список, содержащий цены на товары (10–20 товаров), например:
# [57.8, 46.51, 97, ...]
# Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп
# (например «5 руб 04 коп»). Подумать, как из цены получить рубли и копейки, как добавить нули, если, например,
# получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).
# Вывести цены, отсортированные по возрастанию, новый список не создавать
# (доказать, что объект списка после сортировки остался тот же).
# Создать новый список, содержащий те же цены, но отсортированные по убыванию.
# Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?

user_list = [57.8, 46.51, 97, 15.82, 40, 18.18, 99.99, 155, 658.15, 87]
# Первая часть
for item in  user_list:
    r = int(item)
    kk = round((item - r) * 100)
    print(f'{r} руб. {kk:02d} коп.')
print('--------------------------->')

# Вторая часть
print(id(user_list))
user_list.sort()
print(id(user_list))
for item in  user_list:
    r = int(item)
    kk = round((item - r) * 100)
    print(f'{r} руб. {kk:02d} коп.')
print('--------------------------->')

# Третья часть
new_list = sorted(user_list, reverse=True)
print(new_list)
i = 0
while i < 5:
    r = int(new_list[i])
    kk = round((new_list[i] - r) * 100)
    print(f'{r} руб. {kk:02d} коп.')
    i += 1
