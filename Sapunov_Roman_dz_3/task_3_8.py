# 8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16], [17, 18, 19, 20]]
for row in matrix:
    row.append(sum(row))
    print(row)

# ИЛИ:

column, line = map(int, input('Введите размер матрицы через пробел: ').split())
matrix = []
for i in range(column):
    matrix.append([int(input(f'Заполните матрицу, введя {column * line} чисел: ')) for n in range(line)])
for row in matrix:
    row.append(sum(row))
    print(*row)
