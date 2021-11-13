# Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов,
# взятых из трёх списков (по одному из каждого):
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#         Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках
# (когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?

import random


def get_jokes(number, repeat_joke=True):
    """
    Это функция генерации шуток
    :param number:
    :param repeat_joke:
    :return:
    """
    result = []
    i = 1
    # Проверяем чтобы длина была не больше списка
    if repeat_joke:
        pass
    else:
        if number > len(nouns):
            number = len(nouns)

    while i <= number:
        word1 = random.choice(nouns)
        word2 = random.choice(adverbs)
        word3 = random.choice(adjectives)
        result.append(f'{word1} {word2} {word3}')
        i += 1
        if repeat_joke:
            pass
        else:
            nouns.remove(word1)
            adverbs.remove(word2)
            adjectives.remove(word3)

    return result


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

number_jokes = int(input('Введите количество шуток: '))
print(get_jokes(number_jokes, False))
