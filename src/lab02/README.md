# python_labs
# Лабораторная работа 1
## Задание 1
### Первая функция
```python
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if not nums:
        raise ValueError("Вы не ввели число!")

    min_number = min(nums)
    max_number = max(nums)

    return (min_number, max_number)
```
Считываем дни, считываем возраст, затем вывод эту информацию, предватирительно прибавив один год к возрасту

[![101.png](https://i.postimg.cc/TYjXyxtY/101.png)](https://postimg.cc/4m30MDCr)

### Вторая функция
```python
def unique_sorted(nums: list[float | int]) -> list[float | int]:
    unique_nums = list(set(nums))
    unique_nums.sort()
    return unique_nums

    if not nums:
        raise ValueError("Вы не ввели число!")
```
[![102.png](https://i.postimg.cc/bN0jGPmd/102.png)](https://postimg.cc/bsv5M7cj)

### Третья функция
```python
def flatten(mat: list[list | tuple]) -> list:
    flattened_list = []
    for item in mat:
        if isinstance(item, (list, tuple)):
            flattened_list.extend(item) 
        else:
            raise TypeError("Строка не строка строк матрицы")
    return flattened_list
```
[![103.png](https://i.postimg.cc/Nf8wytd2/103.png)](https://postimg.cc/1fzdTkhy)

## Задание 2
### Первая функция
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
[![201.png](https://i.postimg.cc/c47NKWFg/201.png)](https://postimg.cc/CzK2t3TS)

### Вторая функция
```python
def row_sums(mat: list[list[float | int]]) -> list[float]:
    if not mat:
        return []
    
    # Проверка на прямоугольность
    first_len = len(mat[0])
    for row in mat:
        if len(row) != first_len:
            raise ValueError("Рваная матрица")
    
    return [sum(row) for row in mat]
```
[![202.png](https://i.postimg.cc/L6kMqSxZ/202.png)](https://postimg.cc/3dwq6s5K)

### Третья функция
```python
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
```
[![203.png](https://i.postimg.cc/kgnPKHHJ/203.png)](https://postimg.cc/zVPQ1x56)
