# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь
# ввёл число 3. Считаем 3 + 33 + 333 = 369.

n = input('Введите число: ')

nn = n + n
nnn = nn + n
n = int(n)
nn = int(nn)
nnn = int(nnn)

sum_of_numbers = n + nn + nnn
print(f'Сумма чисел n + nn + nnn равна: {sum_of_numbers}')