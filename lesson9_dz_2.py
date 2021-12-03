# Реализовать класс Road (дорога).
#   1. определить атрибуты: length (длина), width (ширина);
#   2. значения атрибутов должны передаваться при создании экземпляра класса;
#   3. атрибуты сделать защищёнными;
#   4. определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
#   5. использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом,
#      толщиной в 1 см*число см толщины полотна;
#   6. проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.


class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def weight(self):
        mass_of_asphalt = self._length * self._width * 25 * 5
        print(f'Масса асфальта = {self._length} м*{self._width} м *25 кг*5 см = {round(mass_of_asphalt/1000)} т')


mass = Road(20, 5000)
mass.weight()
