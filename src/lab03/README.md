# python_labs
# Лабораторная работа 3
## Задание A
```python
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if not nums:
        raise ValueError("Вы не ввели число!")

    min_number = min(nums)
    max_number = max(nums)

    return (min_number, max_number)
```
Находим минимум и максимум в списке чисел и возвращаем их как кортеж, а если список пуст - вызываем ошибку.

[![103.png](https://i.postimg.cc/Nf8wytd2/103.png)](https://postimg.cc/1fzdTkhy)

## Задание B

```python
def transpose(mat: list[list[float | int]]) -> list[list]:
    if not mat:
        return []
    
    first_len = len(mat[0])
    for row in mat:
        if len(row) != first_len:
            raise ValueError("Рваная матрица")
    
    return [[mat[i][j] for i in range(len(mat))] for j in range(len(mat[0]))]
```
Меняем строки и столбцы местами, проверяя что все строки одинаковой длины.

[![201.png](https://i.postimg.cc/c47NKWFg/201.png)](https://postimg.cc/CzK2t3TS)



