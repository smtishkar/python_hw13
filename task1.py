"""
Задача 3. Создайте класс Матрица.
Добавьте методы для: - вывода на печать,
- сравнения,
- сложения,
- *умножения матриц
"""
import numpy as np


class Matrix:
    rows = None
    columns = None

    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.columns = len(matrix[0])

    
    def __add__(self, other):
    
        try:
            res_matrix = [[0 for _ in range(self.columns)]
                        for _ in range(self.rows)]
            for i in range(self.rows):
                for j in range(self.columns):
                    res_matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
            return res_matrix
        except (ValueError) as e:
            # print('Матрицы разные, сложение не возможно')
            raise ValueError('Матрицы разные, сложение не возможно')
        except(TypeError)as e:
            print(f'введена строка вместо числа по адресу {i,j}. Оштбка {e}')
        except(IndexError) as e:
            print(f'Слишком много значений в матрице по адресу {i,j}. Ошибка - {e}')


    def __mul__(self, other):
        res = np.dot(self.matrix, other.matrix)
        return res

    def __eq__(self, other: "Matrix"):
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError('Матрицы разные, сравнить их не возможно')
        for i in range(self.rows):
            for j in range(self.columns):
                if self.matrix[i][j] != other.matrix[i][j]:
                    return False
        return True

    def __str__(self):
        return f'({self.matrix})'


if __name__ == "__main__":
    try:
        # matrix_1 = Matrix([[4, 7, hjj, 2], [8, 4, 2, 9], [10, 13, 12, 2]])            #Это для проверки NameError
        # matrix_1 = Matrix([[4, 7, 'hjj', 2], [8, 4, 2, 9], [10, 13, 12, 2]])            #Это для проверки TypeError
        # matrix_1 = Matrix([[4, 7, 2,5,7,8], [8, 4, 2, 9], [10, 13, 12, 2]])                   #Это для проверки IndexError
        # matrix_1 = Matrix([[4, 7, 1, 2], [8, 4, 2, 9], [10, 13, 12, 2]])            #Рабочий вариант
        matrix_1 = Matrix([[4, 7, 1], [8, 4, 2, 9], [10, 13, 12, 2]])            #Это для проверки ValueError при сравнении матриц
        matrix_2 = Matrix([[4, 7, 1, 2], [8, 4, 2, 9], [10, 13, 12, 2]])
        print(f"Результат сложения матриц {matrix_1 + matrix_2}")
        print(matrix_1 == matrix_2)
    except(NameError) as e:
        print(f'введена переменная, которая не определена, вместо значения. Ошибка - {e}')

    # matrix_3 = Matrix([[4, 7, 1, 2], [8, 4, 2, 9], [10, 13, 12, 2]])
    # matrix_4 = Matrix([[4, 7, 1], [8, 4, 2], [10, 13, 12], [13, 2, 4]])
    # print(f"Результат перемножения матриц\n{matrix_3*matrix_4}")
    # print(matrix_1 == matrix_2)

