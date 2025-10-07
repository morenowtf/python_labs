"""def transpose(mat: list[list[float | int]]) -> list[list]:
    if not mat:
        return []
    
    # Проверка на прямоугольность
    first_len = len(mat[0])
    for row in mat:
        if len(row) != first_len:
            raise ValueError("Рваная матрица")
    
    # Создаем новую матрицу с размерами MxN -> NxM
    return [[mat[i][j] for i in range(len(mat))] for j in range(len(mat[0]))]

print(transpose([[1, 2, 3]]))
print(transpose([[1], [2], [3]]))
print(transpose([[1, 2], [3, 4]]))
print(transpose([]))
print(transpose([[1, 2], [3]]))"""


"""def row_sums(mat: list[list[float | int]]) -> list[float]:
    if not mat:
        return []
    
    # Проверка на прямоугольность
    first_len = len(mat[0])
    for row in mat:
        if len(row) != first_len:
            raise ValueError("Рваная матрица")
    
    return [sum(row) for row in mat]


print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[-1, 1], [10, -10]]))
print(row_sums([[0, 0], [0, 0]]))
print(row_sums([[1, 2], [3]]))"""


def col_sums(mat: list[list[float | int]]) -> list[float]:
    if not mat:
        return []
    
    # Проверка на прямоугольность
    first_len = len(mat[0])
    for row in mat:
        if len(row) != first_len:
            raise ValueError("Рваная матрица")
    
    # Суммируем элементы по столбцам
    return [sum(mat[i][j] for i in range(len(mat))) for j in range(len(mat[0]))]


print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))
print(col_sums([[1, 2], [3]]))