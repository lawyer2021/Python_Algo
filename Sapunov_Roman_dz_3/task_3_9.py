# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

matrix = [[10, 20, 30, 40], [50, 60, 70, 80], [90, 22, 44, 120], [130, 14, 15, 160]]
for row in matrix:
    print(*row)
columns = []
maxi = []
for i in range(len(matrix)):
    for n in range(len(matrix[i])):
        minimum = matrix[n][i]
        if matrix[n][i] <= minimum:
            columns.append(matrix[n][i])
    print(f"Минимальный элемент столбца № {i+1}, {min(columns)}")
    maxi.append(min(columns))
    columns = []
print("Максимальный элемент среди минимальных: ", max(maxi))
