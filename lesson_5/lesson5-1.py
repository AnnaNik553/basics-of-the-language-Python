"""Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка."""


with open("test.txt", "w", encoding='utf-8') as f_obj:
    data = []
    while True:
        data.append(input('Введите текст '))
        data.append('\n')
        if data[-2] == '':
            data.remove(data[-2])
            break
    f_obj.writelines(data)

print("Текст записан в файл test.txt")
