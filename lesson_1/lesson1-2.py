# Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и
# выведите в формате чч:мм:сс. Используйте форматирование строк.

time_in_seconds = int(input('Введите количество секунд: '))

hours = time_in_seconds // 3600 % 24
minutes = time_in_seconds % 3600 // 60
seconds = time_in_seconds % 60
print(f'{hours:02}:{minutes:02}:{seconds:02}')


