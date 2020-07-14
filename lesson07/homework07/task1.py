# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()), который должен
# принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: см. в методичке.
#
# Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
# первым элементом первой строки второй матрицы и т.д.

class Matrix:

    def __init__(self, array: list):
        self._array = array

    def __str__(self):
        print_string = ''
        for i in range(len(self._array)):
            for j in range(len(self._array[i])):
                print_string = print_string + f'{self._array[i][j]} '
            print_string = print_string + '\n'

        return print_string

    def __add__(self, other):
        result: list = []

        if len(self._array) == len(other._array):
            for i in range(len(self._array)):
                if len(self._array[i]) == len(other._array[i]):
                    str_result: list = []
                    for j in range(len(self._array[i])):
                        str_result.append(self._array[i][j] + other._array[i][j])
                    result.append(str_result)
                else:
                    return f'Не совпадает количество столбцов! Складывать можно только матрицы одинаковой размерности!'
            return result
        else:
            return f'Не совпадает количество строк! Складывать можно только матрицы одинаковой размерности!'


m = Matrix([[1, 6, 3], [8, 2, 7]])

a = Matrix([[8, 1, 5], [6, 9, 12]])

print(m, a, sep='\n')

print(Matrix(m + a))
