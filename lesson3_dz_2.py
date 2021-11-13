# * (вместо задачи 1) Доработать предыдущую функцию в num_translate_adv():
# реализовать корректную работу с числительными,
# начинающимися с заглавной буквы — результат тоже должен быть с заглавной. Например:
# >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"

# Проверяем через istitle(), введенное слово
def num_translate_adv(title_nug):
    if word.istitle():
        return title_nug.title()
    else:
        return title_nug


# lower() - на случай случайного ввода с болшой буквы
def num_translate(eng_nub):
    eng_nub_lower = eng_nub.lower()
    if eng_nub_lower in interpreter:
        return print(num_translate_adv(interpreter[eng_nub_lower]))
    else:
        return None


# Создаем ее в не тела функции чтобы не вызывать каждый раз
interpreter = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}

word = input('Enter the number in English: ')
num_translate(word)
