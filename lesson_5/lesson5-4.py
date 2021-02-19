"""Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно
данные. При этом английские числительные должны заменяться на русские. Новый блок строк
должен записываться в новый текстовый файл."""


with open('1234.txt', encoding='utf-8') as text:
    with open('out_file.txt', 'w', encoding='utf-8') as out_f:
        for line in text:
            if '1' in line:
                line = line.replace('One', 'Один')
                out_f.writelines(line)
            elif '2' in line:
                line = line.replace('Two', 'Два')
                out_f.writelines(line)
            elif '3' in line:
                line = line.replace('Three', 'Три')
                out_f.writelines(line)
            elif '4' in line:
                line = line.replace('Four', 'Четыре')
                out_f.writelines(line)
            print(line.strip())
