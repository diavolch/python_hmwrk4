# Напишите функцию для транспонирования матрицы

matr = [[2, 3, 4], [1, 5, 6]]

def transpose_matr(matr):
    return([list(row) for row in zip(*matr)])

print(transpose_matr(matr))