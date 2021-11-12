# Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
# >>> num_translate("one")
# "один"
# >>> num_translate("eight")
# "восемь"
# Если перевод сделать невозможно, вернуть None.
# Подумайте, как и где лучше хранить информацию, необходимую для перевода:
# какой тип данных выбрать, в теле функции или снаружи.

# lower() - на случай случайного ввода с болшой буквы
def num_translate(eng_nub):
    eng_nub_lower = eng_nub.lower()
    if eng_nub_lower in interpreter:
        return print(interpreter[eng_nub_lower])
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
