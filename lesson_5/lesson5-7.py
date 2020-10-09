"""Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая
строка должна содержать данные о фирме: название, форма собственности, выручка,
издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также
среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать .
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а
также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в
словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{ "firm_1" : 5000 , "firm_2" : 3000 , "firm_3" : 1000 }, { "average_profit" : 2000 }]
Подсказка: использовать менеджер контекста."""

import json

with open("firms.txt", encoding='utf-8') as f_obj:
    firms = f_obj.readlines()
    my_list = [line.split() for line in firms]
    sub = [x[0] for x in my_list]
    list_revenue_cost = [x[2:] for x in my_list]
    profit = []
    for elem in list_revenue_cost:
        new_list_revenue_cost = []
        for el in elem:
            new_list_revenue_cost.append(int(el))
        profit.append(new_list_revenue_cost[0] - new_list_revenue_cost[1])
    dict_firm_profit = dict(zip(sub, profit))
    count_firm = 0
    for i, el in enumerate(profit):
        if el > 0:
            count_firm += 1
    average_profit = sum([x for x in profit if x > 0]) / count_firm
    dict_average_profit = {"average_profit": average_profit}
    list_firm_and_average_profit = [dict_firm_profit, dict_average_profit]
    print(list_firm_and_average_profit)

with open("my_file.json", "w", encoding='utf-8') as write_f:
    json.dump(list_firm_and_average_profit, write_f)
