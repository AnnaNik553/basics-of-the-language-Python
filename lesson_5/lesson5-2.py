"""Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить
подсчет количества строк, количества слов в каждой строке."""


with open('text.txt', encoding='utf-8') as text:
    lines = text.readlines()
    print(f'Количество строк в файле равно {len(lines)}')
    for i, line in enumerate(lines, 1):
        print(f'Количество слов в строке {i} равно {len(line.split())}')
