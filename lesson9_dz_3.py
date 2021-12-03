# Реализовать базовый класс Worker (работник):
#   1. определить атрибуты: name, surname, position (должность), income (доход);
#   2. последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы «оклад»
#      и «премия», например, {"wage": wage, "bonus": bonus};
#   3. создать класс Position (должность) на базе класса Worker;
#   4. в классе Position реализовать методы получения полного имени сотрудника (get_full_name)
#      и дохода с учётом премии (get_total_income);
#   5. проверить работу примера на реальных данных: создать экземпляры класса Position,
#      передать данные, проверить значения атрибутов, вызвать методы экземпляров.

class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        print(f'Имя: {self.name} Фамилия: {self.surname}')

    def get_total_income(self):
        print(f'Дохода {self._income["wage"] + round(self._income["wage"]*self._income["bonus"]/100)}')


# Тут доход в виде процента от оклада
income_user = {"wage": 180000, "bonus": 50}
user = Position('Вася', 'Пупкин', 'Директор', income_user)
user.get_full_name()
user.get_total_income()
