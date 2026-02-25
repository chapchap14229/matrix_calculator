import numpy as np

#умножение матриц
def matrix_multiplication(a,b):
    return a @ b

#умножение матриц на число
def matrix_multiplication_scalar(a,b):
    return a * b

#сложение матриц
def matrix_sum(a,b):
    return a + b

#разность
def diff_matrix(a,b):
    return a - b

#транспонирование
def matrix_transposition(a):
    return a.T

#определитель
def matrix_determenant(a):
    return np.linalg.det(a)

    #обратная матрица
def matrix_invert(a):
    try:
        return np.linalg.inv(a)

    except np.linalg.LinAlgError as e:

        print(f'Ошибка: {str(e)}')
        return None