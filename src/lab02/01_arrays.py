#ПЕРВАЯ ФУНЦИЯ
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    min_number = min(nums)
    max_number = max(nums)

    if not nums:
        raise ValueError("Вы не ввели число!")

    return (min_number, max_number)

#ТЕСТЫ
print(min_max([3, -1, 5, 5, 0]))
print(min_max([42]))
print(min_max([-5, -2, -9]))
print(min_max([1.5, 2, 2.0, -3.1]))
print(min_max([]))


#ВТОРАЯ ФУНКЦИЯ
"""def unique_sorted(nums: list[float | int]) -> list[float | int]:
    unique_nums = list(set(nums))
    unique_nums.sort()
    return unique_nums

    #if not nums:
        #raise ValueError("Вы не ввели число!")

#ТЕСТЫ
print(unique_sorted([3, 1, 2, 1, 3]))
print(unique_sorted([]))
print(unique_sorted([-1, -1, 0, 2, 2]))
print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))"""


#ТРЕТЬЯ ФУНКЦИЯ
"""def flatten(mat: list[list | tuple]) -> list:
    flattened_list = []
    for item in mat:
        if isinstance(item, (list, tuple)):
            flattened_list.extend(item) 
        else:
            raise TypeError("Строка не строка строк матрицы")
    return flattened_list

#ТЕСТЫ
print(flatten([[1, 2], [3, 4]]))
print(flatten(([1, 2], (3, 4, 5))))
print(flatten([[1], [], [2, 3]]))
print(flatten([[1, 2], "ab"]))"""