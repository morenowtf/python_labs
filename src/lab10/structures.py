from collections import deque
from typing import Any

class Stack:
    # Стек (Stack) - структура данных "LIFO" (Last In, First Out)

    
    def __init__(self):
        # Внутреннее хранилище стека
        self._data = []

    def push(self, item):
        # Добавить элемент на вершину стека (в конец) O(1)
        self._data.append(item) # Просто добавляем в конец списка

    def pop(self):
        if self.is_empty():
            raise IndexError("Невозможна операция pop(): стек пуст!")
        return self._data.pop() # pop() без аргументов удаляет последний элемент

    def peek(self):
        # Вернуть верхний элемент без удаления. O(1)
        if self.is_empty():
            return None
        return self._data[-1]

    def is_empty(self) -> bool:
        # Проверить, пуст ли стек. O(1)
        return len(self._data) == 0
    
    def __len__(self) -> int:
        # Количество элементов в стеке. O(1)
        return len(self._data) # Возвращает количество элементов в стеке
    
    def __str__(self) -> str:
        return f"Stack({self._data})" # Строковое представление стека для печати


class Queue:
    # Очередь (Queue) - структура данных "FIFO" (First In, First Out)

    def __init__(self):
        self._data = deque()

    def enqueue(self, item):
        self._data.append(item)  # Добавляем в конец

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Нельзя удалить из пустой очереди!")
        return self._data.popleft()  # Удаляем с начала очереди

    def peek(self):
        if self.is_empty():
            return None
        return self._data[0]  # Вернуть первый элемент без удаления

    def is_empty(self) -> bool:
        return len(self._data) == 0 # Проверить, пуста ли очередь
    
    def __len__(self) -> int:
        return len(self._data) # Возвращает количество элементов в очереди
    
    def __str__(self) -> str:
        return f"Queue({list(self._data)})" # Строковое представление очереди для печати