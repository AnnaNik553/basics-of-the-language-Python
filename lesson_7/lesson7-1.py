"""Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод
__init__() ), который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — с истема некоторых математических величин, расположенных в виде
прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в
привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух
объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой
строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д."""


class Matrix:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return '\n'.join('  '.join(map(str, el)) for el in self.data)

    def __add__(self, other_matrix):
        if len(self.data) == len(other_matrix.data) and len(self.data[0]) == len(other_matrix.data[0]):
            self.result = []
            for i in range(len(self.data)):
                self.temp = []
                for j in range(len(self.data[0])):
                    self.temp.append(self.data[i][j] + other_matrix.data[i][j])
                self.result.append(self.temp)
            return self.result
        else:
            print('мытрицы нельзя складывать')


matrix1 = Matrix([[31, 22], [37, 43], [51, 86]])
matrix2 = Matrix([[30, 21], [36, 42], [50, 85]])
matrix3 = Matrix(matrix1 + matrix2)
print(matrix1, '\n')
print(matrix2, '\n')
print(matrix3, '\n')
