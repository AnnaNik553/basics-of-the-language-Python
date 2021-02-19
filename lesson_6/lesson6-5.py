"""Реализовать класс Stationery ( канцелярская принадлежность). Определить в нем атрибут title
(название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать
три дочерних класса Pen ( ручка), Pencil ( карандаш), Handle ( маркер). В каждом из классов
реализовать переопределение метода draw. Для каждого из классов метод должен выводить
уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный
метод для каждого экземпляра."""


class Stationery:
    def __init__(self, title):
        self.title = title
        self._draw()

    def _draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def _draw(self):
        print('Ручка рисует')


class Pencil(Stationery):
    def _draw(self):
        print('Карандаш рисует')


class Handle(Stationery):
    def _draw(self):
        print('Маркер рисует')


a = Stationery('канцелярская принадлежность')
b = Pen('Ручка')
c = Pencil('Карандаш')
d = Handle('Маркер')
