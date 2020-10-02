# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их
# деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на
# ноль.

def my_division(x, y):
    try:
        return x / y
    except ZeroDivisionError:
          print('division by zero')

a = int(input('Введите а '))
b = int(input('Введите b '))

my_div = my_division(a, b)
print(my_div)
