# Реализовать функцию, принимающую несколько параметров, описывающих данные
# пользователя: имя, фамилия, год рождения, город проживания, email, телефон. Функция
# должна принимать параметры как именованные аргументы. Реализовать вывод данных о
# пользователе одной строкой.

def user_data(**kwargs):
    for key, value in kwargs.items():
        print(f' {key}: {value}', end='  ')

user_data(name='Ales', surname='Smith', year_birth=1990, city='Moscow', email='asmith@gmail.com', phone_number=1111111)
