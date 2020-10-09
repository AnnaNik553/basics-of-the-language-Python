"""Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный
предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их
количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по
нему. Вывести словарь на экран.
Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}"""


with open("school_subjects.txt", encoding='utf-8') as f_obj:
    subjects = f_obj.readlines()
    my_list = [line.split() for line in subjects]
    sub = [x[0] for x in my_list]
    new_sub = [sim.replace(':', '') for sim in sub]
    num = [x[1:] for x in my_list]
    new_num = []
    for numbers in num:
        new_el = []
        for el in numbers:
            el = ''.join(x for x in el if x.isdigit())
            if el == '':
                continue
            el = int(el)
            new_el.append(el)
        new_num.append(sum(new_el))
    print(dict(zip(new_sub, new_num)))
