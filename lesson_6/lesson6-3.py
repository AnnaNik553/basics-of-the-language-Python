"""Реализовать базовый класс Worker ( работник), в котором определить атрибуты: name,
surname, position ( должность), income ( доход). Последний атрибут должен быть
защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например,
{"wage": wage, "bonus": bonus}. Создать класс Position ( должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника ( get_full_name) и
дохода с учетом премии ( get_total_income) . Проверить работу примера на реальных данных
(создать экземпляры класса Position , передать данные, проверить значения атрибутов,
вызвать методы экземпляров)."""


class Worker:
    def __init__(self, name, surname, position, income={"wage": 0, "bonus": 0}):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        print(self.name, self.surname)

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


a = Position('Sam', 'Smith', 'Analyst')
a._income['wage'] = 50000
a._income['bonus'] = 10000
a.get_full_name()
print(a.get_total_income())