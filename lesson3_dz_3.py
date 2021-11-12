# Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
# в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
# Например:
# >>>  thesaurus("Иван", "Мария", "Петр", "Илья")
# {
#     "И": ["Иван", "Илья"],
#     "М": ["Мария"], "П": ["Петр"]
# }
# Подумайте: полезен ли будет вам оператор распаковки? Как поступить,
# если потребуется сортировка по ключам? Можно ли использовать словарь в этом случае?

def thesaurus(*names):
    notebook = {}
    user_list = [*names]
    print(user_list)
    for name in user_list:
        first_letter = name[0]
        if first_letter in notebook:
            names = notebook[first_letter]
            names.append(name)
        else:
            notebook[first_letter] = [name]
    return notebook


user_notebook = thesaurus("Петр", "Илья", "Маша", "Иван", "Мария")
print(user_notebook)

# Сортируем по ключу
notebook_list = list(user_notebook)
notebook_list.sort()
for i in notebook_list:
    print(f'{i} : {user_notebook[i]}')
