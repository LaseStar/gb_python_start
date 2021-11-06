# Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
# Внимание: использовать только арифметические операции!
# К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка,
# сумма цифр которых делится нацело на 7.
# * Решить задачу под пунктом b, не создавая новый список

# создаем список из нечетных чисел
# numbers_list = [19, 49, 15, 665, 19]
# Изменил просмотрев меточку №2, видимо авто пишит создать == автоматически
# а создать вручную != автоматически
numbers_list = []
for _ in range(1, 1000, 2):
    numbers_list.append(_)

print(numbers_list)

# создаем новый списк для хранения кубов этих чисел
numbers_cube_list = []
for idx in range(len(numbers_list)):
    number_cube = numbers_list[idx] ** 3
    # Исли надо добавить 17
    # number_cube = numbers_list[idx] ** 3 + 17
    numbers_cube_list.append(number_cube)

# Можно сразу было сделать проще
# numbers_cube_list = [19 ** 3 + 17, 49 ** 3 + 17, 15 ** 3 + 17, 665 ** 3 + 17, 19 ** 3 + 17]

print(numbers_cube_list)

# Проходим по списку получаем каждое число
result = 0
for number in numbers_cube_list:
    _sum = 0
    i = 1

    # тут воспользуемся while и арифметические операции
    while i <= len(str(number)):
        _sum += number % 10 ** i // 10 ** (i - 1)
        i += 1

    # проверяем условия
    if _sum % 7 == 0:
        print(number, ' выполняет условие')
        result += number

# Так для красоты
print('------------------------>')

# выводим результат
print('Сумма чисел равна: ', result)
