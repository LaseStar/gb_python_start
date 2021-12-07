# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для  сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно.
# Первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и пр.

class Matrix:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        str_matrix = ''
        for row in self.data:
            str_matrix += '  '.join(map(str, row)) + '\n'
        return str_matrix

    def __add__(self, other):
        if len(self.data) == len(other.data) and len(self.data[0]) == len(other.data[0]):
            data = []

            for j in range(len(self.data)):
                data.append([])
                for k in range(len(self.data[0])):
                    data[j].append(self.data[j][k] + other.data[j][k])

            return Matrix(data)
        else:
            raise ValueError('Несоответствие размеров матриц')


m1 = [[31, 22], [37, 43], [51, 86]]
m2 = [[3, 5, 32], [2, 4, 6], [-1, 64, -8]]
m2_2 = [[5, 15, -32], [8, 8, 9], [10, 6, -81]]
m3 = [[3, 5, 8, 3], [8, 3, 7, 1]]

matr_1 = Matrix(m1)
print(matr_1)

matr_2 = Matrix(m2)
print(matr_2)

matr_2_2 = Matrix(m2_2)
print(matr_2_2)

print('Сложение:')
print(matr_2 + matr_2_2)

matr_3 = Matrix(m3)
print(matr_3)
