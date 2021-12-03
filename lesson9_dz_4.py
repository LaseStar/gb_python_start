# Реализуйте базовый класс Car:
#   1. у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
#      А также методы: go, stop, turn(direction), которые должны сообщать,
#      что машина поехала, остановилась, повернула (куда);
#   2. опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
#   3. добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
#   4. для классов TownCar и WorkCar переопределите метод show_speed.
#      При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = int(speed)
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print(f'Машина повернула {direction}')

    def show_speed(self):
        print(f'Скорость автомобиля {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'{self.color} автомобиль {self.name} превысел скорость на {self.speed-60}')


class SportCar(Car):
    def infra(self):
        print(f'Спортивная {self.color} {self.name}')


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'{self.color} автомобиль {self.name} превысел скорость на {self.speed-40}')


class PoliceCar(Car):
    def infra(self):
        print(f'Полицейская {self.color} {self.name}')


town_car = TownCar('75', 'бежевая', 'жигули')
town_car.show_speed()
print('------------')

workCar = WorkCar(62, 'желтый', 'погрузчик')
workCar.show_speed()
print('------------')

police = PoliceCar(90, 'синий', 'Porsche', True)
police.infra()
police.show_speed()
print('------------')

ferrari = SportCar(180, 'красный', 'Ferrari')
ferrari.infra()
ferrari.show_speed()
print('------------')
