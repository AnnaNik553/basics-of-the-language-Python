"""Реализовать класс Road ( дорога), в котором определить атрибуты: length ( длина), width
(ширина). Значения данных атрибутов должны передаваться при создании экземпляра
класса. Атрибуты сделать защищенными. Определить метод расчета массы асфальта,
необходимого для покрытия всего дорожного полотна. Использовать формулу:
длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в
1 см*число см толщины полотна. Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т"""


class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_mass_asphalt(self):
        print(f'масса асфальта для покрытия дороги длиной {self._length}м и шириной {self._width}м равна {self._length*self._width*25*5/1000} т')


a = Road(5000, 20)
a.calc_mass_asphalt()