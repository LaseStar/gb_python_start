# (вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield.

max_number = int(input('Введите число для генератора: '))
odd_to = (num for num in range(1, max_number + 1, 2))
for i in odd_to:
    print(i)
