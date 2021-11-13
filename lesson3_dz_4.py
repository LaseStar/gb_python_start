# * (вместо задачи 3) Написать функцию thesaurus_adv(),
# принимающую в качестве аргументов строки в формате «Имя Фамилия» и возвращающую словарь,
# в котором ключи — первые буквы фамилий, а значения — словари,
# реализованные по схеме предыдущего задания и содержащие записи,
# в которых фамилия начинается с соответствующей буквы. Например:
# >>>thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
# {
#     "А": {
#         "П": ["Петр Алексеев"]
#     },
#     "С": {
#         "И": ["Иван Сергеев", "Инна Серова"],
#         "А": ["Анна Савельева"]
#     }
# }
# Как поступить, если потребуется сортировка по ключам?


def thesaurus_adv(*names_surnames):
    # Формируем основной список
    result_notebook = {}
    user_list = [*names_surnames]
    for word in user_list:
        name_surname = word.split()
        surname = name_surname[1]
        first_letter_s = surname[0]
        if first_letter_s in result_notebook:
            names = result_notebook[first_letter_s]
            names.append(word)
        else:
            result_notebook[first_letter_s] = [word]

    # Формируем вспомогательный список
    for idx, item in result_notebook.items():
        notebook = {}
        for name in item:
            first_letter = name[0]
            if first_letter in notebook:
                names = notebook[first_letter]
                names.append(name)
            else:
                notebook[first_letter] = [name]
        result_notebook[idx] = notebook

    return result_notebook


def thesaurus_adv_teacher(*names_surnames):
    result_notebook = {}
    for name_surname in names_surnames:
        name, surname = name_surname.split()
        result_notebook.setdefault(surname[0], {})
        result_notebook[surname[0]].setdefault(name[0], [])
        result_notebook[surname[0]][name[0]].append(name_surname)

    return result_notebook


# user_notebook = thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
user_notebook = thesaurus_adv_teacher("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
print(user_notebook)

# Сортируем по ключу
notebook_list = list(user_notebook)
notebook_list.sort()
for i in notebook_list:
    print(f'{i} : ')
    user_notebook2 = user_notebook[i]
    notebook_list2 = list(user_notebook[i])
    notebook_list2.sort()
    print(notebook_list2)
    for _ in notebook_list2:
        print(f'{_} : {user_notebook2[_]}')
