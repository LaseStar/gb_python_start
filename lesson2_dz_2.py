# Дан список:
# ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# Необходимо его обработать — обособить каждое целое число (вещественные не трогаем)
# кавычками (добавить кавычку до и кавычку после элемента списка, являющегося числом)
# и дополнить нулём до двух целочисленных разрядов:
# ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
#
# Сформировать из обработанного списка строку:
# в "05" часов "17" минут температура воздуха была "+05" градусов
#
# Подумать, какое условие записать, чтобы выявить числа среди элементов списка?
# Как модифицировать это условие для чисел со знаком?
# Примечание: если обособление чисел кавычками не будет получаться - можете вернуться к его реализации позже.
# Главное: дополнить числа до двух разрядов нулём!

user_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# Создаем новый список
new_list = []
# пишем цикл для выполнения условия задачи
for item in user_list:
    # Можно через функцию isdigit()
    # if item.isdigit():
    #     number = int(item)
    #     new_list.append('"')
    #     if len(str(number)) != len(item):
    #         new_list.append(f'+{number:02d}')
    #     else:
    #         new_list.append(f'{number:02d}')
    #     new_list.append('"')
    # else:
    #     new_list.append(item)

    # Но мне так больше нравится ))
    try:
        number = int(item)
        new_list.append('"')
        if len(str(number)) != len(item):
            new_list.append(f'+{number:02d}')
        else:
            new_list.append(f'{number:02d}')
        new_list.append('"')
    except ValueError:
        new_list.append(item)
# Выводим список
message = ''
message = ' '.join(new_list)

print(message)
