# Реализовать склонение слова «процент» во фразе «N процентов».
# Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100:

# Создаем список из слов
percent_list = [' процент ', 'процента', 'процентов']

# прогоняем список от 1 до 100 и выводим результат
for i in range(1, 101):
    if i == 1:
        name_percent = percent_list[0]
    elif i < 5:
        name_percent = percent_list[1]
    else:
        name_percent = percent_list[2]
    print(f'{i} {name_percent}')
