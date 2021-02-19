# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и
# возвращает сумму наибольших двух аргументов.

def my_func(a, b, c):
    min_el = min(a, b, c)
    my_sum = a + b + c - min_el
    return my_sum

print(my_func(5, 6, 7))
