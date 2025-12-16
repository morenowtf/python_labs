from collections import deque
from typing import Any

class Stack:
    """
    Стек (Stack) - структура данных "LIFO" (Last In, First Out).
    Последний пришел - первый вышел.
    Представь стопку тарелок: новую кладешь сверху, и сверху же забираешь.
    """
    
    def __init__(self):
        # внутреннее хранилище стека
        self._data = []

    def push(self, item):
        # корректно: добавление в конец списка O(1) амортизированно
        self._data.append(item) # Просто добавляем в конец списка

    def pop(self):
        if self.is_empty():
            raise IndexError("Невозможна операция pop(): стек пуст!")
        return self._data.pop() # pop() без аргументов удаляет последний элемент

    def peek(self):
        # ошибка: при пустом стеке будет IndexError — желательно вернуть None
        if self.is_empty():
            return None
        return self._data[-1]

    def is_empty(self) -> bool:
        # TODO: улучшить реализацию
        return len(self._data) == 0
    
    def __len__(self) -> int:
        return len(self._data) #Возвращает количество элементов в стеке
    
    def __str__(self) -> str:
        return f"Stack({self._data})" #Строковое представление стека для печати


class Queue:
    """
    Очередь (Queue) - структура данных "FIFO" (First In, First Out).
    Первый пришел - первый вышел.
    Представь очередь в магазине: кто первый встал, того первым обслужат.
    """
    
    def __init__(self):
        """
        Инициализация пустой очереди.
        Используем deque (двустороннюю очередь) из collections.
        Почему не список? Потому что удаление из начала списка - O(n), а у deque - O(1).
        """
        self._data = deque()  # deque - оптимизирован для операций с обоих концов

    def enqueue(self, item):
        # ошибка: вставка в начало, а не в конец
        self._data.append(item)  # Добавляем в конец

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Нельзя удалить из пустой очереди!")
        return self._data.popleft()  # Удаляем СЛЕВА (начало очереди)

    def peek(self):
        if self.is_empty():
            return None
        return self._data[0]  # Первый элемент

    def is_empty(self) -> bool:
        return len(self._data) == 0
    
    def __len__(self) -> int:
        return len(self._data) #Возвращает количество элементов в очереди
    
    def __str__(self) -> str:
        return f"Queue({list(self._data)})" #Строковое представление очереди для печати.