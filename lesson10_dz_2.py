# Реализовать проект расчёта суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке знания.
# Реализовать абстрактные классы для основных классов проекта и проверить работу декоратора @property.

from abc import ABC, abstractmethod


class Сlothes(ABC):

    def __init__(self, name='', param=0):
        self.name = name
        self.param = param
        self._res_sum = []

    @abstractmethod
    def fabric_length(self):
        return self.param

    def __add__(self, other):
        self._res_sum.append(other.fabric_length())
        return self

    def __str__(self):
        return f'{self.name} параметр {self.param}'

    @property
    def res_sum(self):
        return round(sum(self._res_sum), 2)


class Coat(Сlothes):
    def __str__(self):
        return f'{self.name} р-р {self.param}'

    def fabric_length(self):
        return round(self.param / 6.5 + 0.5, 2)


class Costume(Сlothes):
    def __str__(self):
        return f'{self.name} рост {self.param}'

    def fabric_length(self):
        return round(2 * self.param + 0.3, 2)


# Создаем первый элемент пустым чтобы сработал __add__
cloth = Coat()
cloth1 = Coat('Мужское пальто', 50)
cloth2 = Coat('Женсоке пальто', 44)
cloth3 = Costume('Мужское костюм', 50)

print(cloth1)
print(cloth1.fabric_length())
print(cloth2)
print(cloth2.fabric_length())
print(cloth3)
print(cloth3.fabric_length())
print('--------------------')
cloth + cloth1 + cloth2 + cloth3

print(cloth.res_sum)
