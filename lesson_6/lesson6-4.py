"""Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed,
color, name, is_police ( булево). А также методы: go, stop, turn(direction), которые должны
сообщать, что машина поехала, остановилась, повернула (куда). Опишите несколько
дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод
show_speed, который должен показывать текущую скорость автомобиля. Для классов
TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60
( TownCar ) и 40 ( WorkCar ) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к
атрибутам, выведите результат. Выполните вызов методов и также покажите результат."""


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('машина поехала')

    def stop(self):
        print('машина остановилась')

    def turn(self, direction):  # лево / право
        self.direction = direction
        print(f'машина повернула на {self.direction}')

    def show_speed(self):
        print(f'скорость автомобиля {self.speed}')


class TownCar(Car):
    def show_speed(self):
        print(f'скорость автомобиля {self.speed}')
        if self.speed > 60:
            print('превышение скорости. скорость свыше 60')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print(f'скорость автомобиля {self.speed}')
        if self.speed > 40:
            print('превышение скорости. скорость свыше 40')


class PoliceCar(Car):
    pass


a = Car(50, 'black', 'Audi')
a.go()
a.stop()
a.turn('право')
a.show_speed()

b = TownCar(70, 'rad', 'Audi')
b.go()
b.stop()
b.turn('лево')
b.show_speed()

c = WorkCar(60, 'white', 'Audi')
c.go()
c.stop()
c.turn('лево')
c.show_speed()
