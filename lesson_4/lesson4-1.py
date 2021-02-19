"""Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной
платы сотрудника. В расчете необходимо использовать формулу: (выработка в часах*ставка в
час) + премия. Для выполнения расчета для конкретных значений необходимо запускать
скрипт с параметрами."""

from sys import argv

my_working_hours, my_hourly_rate, my_bonus = argv[1:]


def salary(working_hours, hourly_rate, bonus):
    working_hours, hourly_rate, bonus = float(working_hours), float(hourly_rate), float(bonus)
    my_salary = round((working_hours * hourly_rate + bonus), 2)
    return my_salary


print(f'Заработная плата сотрудника составляет: {salary(my_working_hours, my_hourly_rate, my_bonus)}')
