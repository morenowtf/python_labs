# Лабораторная работа 2
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
Находим минимум и максимум в списке чисел и возвращаем их как кортеж, а если список пуст - вызываем ошибку.

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
Преобразуем список в множество чтобы убрать дубликаты, затем обратно в список и сортируем по возрастанию.

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
Проходим по всем элементам входного списка, проверяем что каждый элемент является списком или кортежем, и если да - добавляем его элементы в результирующий список, иначе выдаём ошибку.

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
Меняем строки и столбцы местами, проверяя что все строки одинаковой длины.

[![201.png](https://i.postimg.cc/c47NKWFg/201.png)](https://postimg.cc/CzK2t3TS)

### Вторая функция
```python
def row_sums(mat: list[list[float | int]]) -> list[float]:
    if not mat:
        return []
    
    first_len = len(mat[0])
    for row in mat:
        if len(row) != first_len:
            raise ValueError("Рваная матрица")
    
    return [sum(row) for row in mat]
```
Суммируем элементы каждой строки, проверяя что матрица прямоугольная.

[![202.png](https://i.postimg.cc/L6kMqSxZ/202.png)](https://postimg.cc/3dwq6s5K)

### Третья функция
```python
if not mat:
        return []
    
    first_len = len(mat[0])
    for row in mat:
        if len(row) != first_len:
            raise ValueError("Рваная матрица")
    
    return [sum(mat[i][j] for i in range(len(mat))) for j in range(len(mat[0]))]
```
Суммируем элементы каждого столбца, проверяя что матрица прямоугольная.

[![203.png](https://i.postimg.cc/kgnPKHHJ/203.png)](https://postimg.cc/zVPQ1x56)

## Задание 3
```python
def format_record(rec: tuple[str, str, float]) -> str:
    fio, group, gpa = rec
    
    if not fio or not fio.strip():
        raise ValueError("ФИО не может быть пустым")
    if not group or not group.strip():
        raise ValueError("Группа не может быть пустой")
    if not isinstance(gpa, (int, float)):
        raise TypeError("GPA должно быть числом")
    
    fio_parts = ' '.join(fio.split()).title().split()
    
    if len(fio_parts) == 3:
        initials = f"{fio_parts[1][0]}.{fio_parts[2][0]}."
    elif len(fio_parts) == 2:
        initials = f"{fio_parts[1][0]}."
    else:
        raise ValueError("ФИО должно содержать 2 или 3 части")
    
    formatted_gpa = f"{gpa:.2f}"
    
    return f"{fio_parts[0]} {initials}, гр. {group.strip()}, GPA {formatted_gpa}"
```
Извлекаем ФИО, группу и GPA из кортежа, проверяем их корректность, обрабатываем ФИО для формирования инициалов, форматируем GPA до двух знаков и собираем всё в требуемую строку.

[![301.png](https://i.postimg.cc/Bbgn3MB6/301.png)](https://postimg.cc/9wDhtPS5)






