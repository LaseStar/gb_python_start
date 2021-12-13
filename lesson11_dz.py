# """
# == Лото ==
# Правила игры в лото.
# Игра ведется с помощью спе циальных карточек, на которых отмечены числа,
# и фишек (бочонков) с цифрами.
# Количество бочонков — 90 штук (с цифрами от 1 до 90).
# Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
# расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
#
# --------------------------
#     9 43 62          74 90
#  2    27    75 78    82
#    41 56 63     76      86
# --------------------------
#
# В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
# случайная карточка.
#
# Каждый ход выбирается один случайный бочонок и выводится на экран.
# Также выводятся карточка игрока и карточка компьютера.
#
# Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
# Если игрок выбрал "зачеркнуть":
#     Если цифра есть на карточке - она зачеркивается и игра продолжается.
#     Если цифры на карточке нет - игрок проигрывает и игра завершается.
# Если игрок выбрал "продолжить":
#     Если цифра есть на карточке - игрок проигрывает и игра завершается.
#     Если цифры на карточке нет - игра продолжается.
#
# Побеждает тот, кто первый закроет все числа на своей карточке.
# Пример одного хода:
# Новый бочонок: 70 (осталось 76)
# ------ Ваша карточка -----
#  6  7          49    57 58
#    14 26     -    78    85
# 23 33    38    48    71
# --------------------------
# -- Карточка компьютера ---
#  7 87     - 14    11
#       16 49    55 88    77
#    15 20     -       76  -
# --------------------------
# Зачеркнуть цифру? (y/n)
#
# Подсказка: каждый следующий случайный бочонок из мешка удобно получать
# с помощью функции-генератора.
#
# Подсказка: для работы с псевдослучайными числами удобно использовать
# модуль random: http://docs.python.org/3/library/random.html
import time
from random import randint
import json


def unique_lis(all_num, unique_num):
    user_list = []
    while len(user_list) <= unique_num:
        rand_num = randint(1, all_num)
        if rand_num not in user_list:
            user_list.append(rand_num)
    return user_list


class Card:

    def __init__(self, lev):
        if lev == 1:
            self.rows = 3
            self.num_in_row = 5
        elif lev == 2:
            self.rows = 3
            self.num_in_row = 6
        elif lev == 3:
            self.rows = 3
            self.num_in_row = 7
        elif lev == 4:
            self.rows = 4
            self.num_in_row = 6
        else:
            self.rows = 5
            self.num_in_row = 7

        self.cols = self.num_in_row + 4
        self.delimit = self.cols * 3 - 1
        self.all_num = 90
        self.emptiness = 0
        self.dash = -1

        unique_nums = self.rows * self.num_in_row
        non_recurring = unique_lis(self.all_num, unique_nums)
        self.data = self.fill_list(non_recurring)

    def __str__(self):
        delimiter = '-'*self.delimit
        ret = delimiter + '\n'
        for index, num in enumerate(self.data):
            if num == self.emptiness:
                ret += '  '
            elif num == self.dash:
                ret += ' -'
            elif num < 10:
                ret += f' {str(num)}'
            else:
                ret += str(num)

            if (index + 1) % self.cols == 0:
                ret += '\n'
            else:
                ret += ' '

        return ret + delimiter

    def fill_list(self, non_list):
        new_list = []
        empty = self.cols - self.num_in_row
        for i in range(self.rows):
            row_num = sorted(non_list[self.num_in_row * i: self.num_in_row * (i + 1)])
            for _ in range(empty):
                ind = randint(0, len(row_num))
                row_num.insert(ind, self.emptiness)
            new_list += row_num
        return new_list

    def cross_num(self, num):
        for index, item in enumerate(self.data):
            if item == num:
                self.data[index] = self.dash

    def __contains__(self, item):
        return item in self.data

    def closed(self):
        return set(self.data) == {self.emptiness, self.dash}


class Game:

    def __init__(self, lev):
        self.user_card = Card(lev)
        self.comp_card = Card(lev)
        self.kegs = unique_lis(90, 89)

    def play(self):
        """
        :return:
        0 - игра продолжаентся
        1 - выграл user
        2 - выграл компьютер
        """

        keg = self.kegs.pop()
        print(f'Новый бочонок: {keg} (осталось {len(self.kegs)})')
        print(f'----- Ваша карточка ------\n{self.user_card}')
        print(f'-- Карточка компьютера ---\n{self.comp_card}')

        user_answer = input('Зачеркнуть цифру? (y/n)').lower().strip()
        if user_answer == 'y' and keg not in self.user_card or user_answer != 'y' and keg in self.user_card:
            return 2

        if keg in self.user_card:
            self.user_card.cross_num(keg)
            if self.user_card.closed():
                return 1

        if keg in self.comp_card:
            self.comp_card.cross_num(keg)
            if self.comp_card.closed():
                return 2

        return 0


try:
    with open('tournament_table.json', 'r', encoding='utf-8') as tt:
        list_tt = json.loads(tt.read())
except FileNotFoundError:
    list_tt = []

list_tt.sort(key=lambda i: i[1])
print('------------------------------')
print('       Турнирная таблица      ')
print('------------------------------')
for _ in list_tt:
    print(*_)
print('------------------------------')

user_name = input('Введите свое имя: ')
level = int(input('Выберите уровень от 1 до 5: '))
if 0 < level <= 5:
    game = Game(level)
    star_time = time.time()
    while True:
        score = game.play()
        if score == 1:
            print('Ты выиграл!!!')
            finish_time = time.time()
            list_tt.append([user_name, round(finish_time - star_time), ' секунд'])
            with open('tournament_table.json', 'w') as tt:
                json.dump(list_tt[:5], tt)
            break
        elif score == 2:
            print('Ты проиграл (((')
            finish_time = time.time()
            break

    print('Затрачено ', round(finish_time - star_time), ' секунд')
else:
    print('Не правильно выбран уровень')
