"""Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить
ее на экран."""


with open("sum_of_numbers.txt", "w+", encoding='utf-8') as f_obj:
    f_obj.write(input('Введите числа через пробел '))
    f_obj.seek(0)
    numbers = f_obj.read()
    print(f'Сумма чисел равна {round(sum([float(num) for num in numbers.split()]), 2)}')
