# * (вместо задачи 2) Решить задачу 2 не создавая новый список (как говорят, in place).
# Эта задача намного серьёзнее, чем может сначала показаться.

# user_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
user_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# пишем цикл для выполнения условия задачи
i = 0
while i <= len(user_list)-1:
    try:
        item = user_list[i]
        number = int(item)
        user_list.insert(i, '"')
        if len(str(number)) != len(item):
            user_list[i+1] = f'+{number:02d}'
        else:
            user_list[i+1] = f'{number:02d}'
        user_list.insert(i+2, '"')
        i += 2
    except ValueError:
        i += 1

# Выводим список
message = ''
message = ' '.join(user_list)
print(message)
