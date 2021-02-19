"""Создать текстовый файл (не программно), построчно записать фамилии сотрудников и
величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее
20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода
сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32"""

with open('list_of_staff.txt', encoding='utf-8') as file:
    staff_list = file.readlines()
    staff_salary = dict( [x.split() for x in staff_list] )
    new_staff_salary = {k: float(v) for k, v in staff_salary.items()}
    for i, j in new_staff_salary.items():
        if j < 20000:
            print(f'оклад менее 20 тыс. у сотрудника {i}')

    print(f'средняя величина дохода сотрудников {round(sum(new_staff_salary.values()) / len(new_staff_salary), 2)}')
