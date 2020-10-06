"""Реализовать формирование списка, используя функцию range() и возможности генератора. В
список должны войти четные числа от 100 до 1000 (включая границы). Необходимо получить
результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce() ."""

from functools import reduce

# 0
new_list = [i for i in range(100, 1001, 2)]
print(new_list)

def my_f(num1, num2):
    return num1 * num2

print(reduce(my_f, new_list))

# 1
new_list = [reduce(lambda x, y: x*y, range(100, 1001, 2)) for i in range(1)]
print(new_list)
