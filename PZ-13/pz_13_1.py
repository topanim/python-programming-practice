"""
В двумерном списке найти суммы элементов каждой строки и поместить их в новый массив.
Выполнить замену элементов третьего столбца исходной матрицы на полученные суммы.
"""

# Суммы строк матрицы и замена третьего столбца
try:
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]  # Пример матрицы
    print("Исходная матрица:")
    for row in matrix: print(row)

    # Проверяем, что матрица имеет хотя бы 3 столбца
    if not matrix or len(matrix[0]) < 3:
        raise ValueError("Матрица должна иметь минимум 3 столбца")

    # Находим суммы строк
    row_sums = [sum(row) for row in matrix]
    print("Массив сумм строк:", row_sums)

    # Заменяем элементы третьего столбца (индекс 2) на суммы
    for i in range(len(matrix)):
        matrix[i][2] = row_sums[i]

    print("Результирующая матрица:")
    for row in matrix: print(row)

except (TypeError, ValueError) as e:
    print(f"Ошибка: {e}")