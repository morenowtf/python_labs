# Лабораторная работа 10

## Теоретическая часть

### Стек (Stack)
- **Что это**: Структура данных LIFO (Last In, First Out) - "последним пришел, первым ушел"
- **Аналогия**: Стопка тарелок - новую кладем сверху, и сверху же берем
- **Основные операции**:
  - `push(item)` - добавить на вершину (O(1))
  - `pop()` - снять с вершины (O(1))
  - `peek()` - посмотреть вершину без удаления (O(1))

### Очередь (Queue)
- **Что это**: Структура данных FIFO (First In, First Out) - "первым пришел, первым ушел"
- **Аналогия**: Очередь в магазине - кто первый встал, того первым обслужили
- **Основные операции**:
  - `enqueue(item)` - добавить в конец (O(1))
  - `dequeue()` - взять из начала (O(1))
  - `peek()` - посмотреть первый элемент (O(1))

### Связный список (Singly Linked List)
- **Что это**: Цепочка узлов, где каждый узел содержит значение и ссылку на следующий узел
- **Структура**: `[значение|ссылка] -> [значение|ссылка] -> [значение|None]`
- **Основные операции**:
  - `append(value)` - добавить в конец (O(1) с tail, O(n) без tail)
  - `prepend(value)` - добавить в начало (O(1))
  - `insert(idx, value)` - вставить по индексу (O(n))
  - `remove_at(idx)` - удалить по индексу (O(n))

# Практика

## Structures.py
```python
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
```

Этот код создаёт две основные структуры данных - стек (где элементы работают по принципу "последний зашёл, первый вышел") и очередь (где "первый зашёл, первый вышел") - с базовыми операциями добавления, удаления и проверки элементов.

## Тест

``` python
from src.lab10.structures import Stack, Queue
from src.lab10.linked_list import SinglyLinkedList

# Тест Stack
print("=== Тест Stack ===")
s = Stack()

# Проверяем пустой стек
print("1. Пустой стек:")
print(f"   is_empty = {s.is_empty()}")  # True
print(f"   peek = {s.peek()}")          # None

# Добавляем элементы
print("\n2. Добавляем 1, 2, 3:")
s.push(1)
s.push(2)
s.push(3)
print(f"   Стек: {s}")
print(f"   Длина: {len(s)}")            # 3
print(f"   peek = {s.peek()}")          # 3

# Удаляем элементы
print("\n3. Удаляем элементы:")
print(f"   pop = {s.pop()}")            # 3
print(f"   pop = {s.pop()}")            # 2
print(f"   Осталось: {s}")

# Проверяем ошибку
print("\n4. Проверка ошибки:")
s.pop()  # удаляем последний
try:
    s.pop()
except IndexError as e:
    print(f"   Ошибка при pop из пустого стека: {e}")

# Тест Queue
print("\n=== Тест Queue ===")
q = Queue()

# Проверяем пустую очередь
print("1. Пустая очередь:")
print(f"   is_empty = {q.is_empty()}")  # True
print(f"   peek = {q.peek()}")          # None

# Добавляем элементы
print("\n2. Добавляем 'a', 'b', 'c':")
q.enqueue('a')
q.enqueue('b')
q.enqueue('c')
print(f"   Очередь: {q}")
print(f"   Длина: {len(q)}")            # 3
print(f"   peek = {q.peek()}")          # 'a'

# Удаляем элементы
print("\n3. Удаляем элементы:")
print(f"   dequeue = {q.dequeue()}")    # 'a'
print(f"   dequeue = {q.dequeue()}")    # 'b'
print(f"   Осталось: {q}")

# Еще раз проверяем peek и is_empty
print("\n4. Проверяем состояние:")
q.enqueue('d')
print(f"   Добавили 'd': {q}")
print(f"   peek = {q.peek()}")          # 'c'
print(f"   is_empty = {q.is_empty()}")  # False

# Проверяем ошибку
print("\n5. Проверка ошибки:")
q.dequeue()  # 'c'
q.dequeue()  # 'd'
try:
    q.dequeue()
except IndexError as e:
    print(f"   Ошибка при dequeue из пустой очереди: {e}")
```

[![34564645.png](https://i.postimg.cc/x1rZsfWQ/34564645.png)](https://postimg.cc/563pyV4K)


## Linked_list.py
```python
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None  # Хвост - для оптимизации добавления в конец
        self._size = 0  # Начинаем с 0 элементов

    def append(self, value):
        """Добавить элемент в конец списка"""
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:  # Если в списке уже есть элементы
            self.tail.next = new_node  # Старый хвост теперь указывает на новый узел
            self.tail = new_node  # Новый узел становится хвостом
        
        self._size += 1  # Не забываем увеличить счетчик!
        

    def prepend(self, value):
        new_node = Node(value)
        
        if self.head is None:  # Если список пустой
            self.head = new_node
            self.tail = new_node
        else:  # Если в списке уже есть элементы
            new_node.next = self.head  # Новый узел указывает на старую голову
            self.head = new_node  # Новый узел становится головой
        
        self._size += 1

    def insert(self, idx, value):
        """Вставка по индексу O(n)"""
        # Проверяем, что индекс в допустимых пределах
        if idx < 0 or idx > self._size:
            raise IndexError(f"Index {idx} out of range [0, {self._size}]")
        
        # Если вставляем в начало
        if idx == 0:
            self.prepend(value)
            return
        
        if idx == self._size:
            self.append(value)
            return
        
        # Ищем позицию для вставки
        current = self.head
        # Переходим к узлу перед нужной позицией
        for _ in range(idx - 1):
            current = current.next
        
        # Вставляем новый узел
        new_node = Node(value, next=current.next)
        current.next = new_node
        
        # ИСПРАВЛЕНО: увеличиваем размер
        self._size += 1

    def __iter__(self):
        """Итератор по значениям списка"""
        current = self.head
        while current is not None:
            yield current.value
            current = current.next

    def __len__(self):
        """Возвращает количество элементов O(1)"""
        return self._size

    def __repr__(self):
        """Строковое представление списка"""
        values = list(self)
        return f"SinglyLinkedList({values})"
```

Этот код создаёт односвязный список, в котором можно добавлять элементы в начало, конец или в любое место по индексу, поддерживая их последовательную связь через узлы.

## Тест

``` python
print("=== Тест SinglyLinkedList ===")
lst = SinglyLinkedList()

# Проверяем пустой список
print("1. Пустой список:")
print(f"   Список: {lst}")
print(f"   Длина: {len(lst)}")          # 0

# Добавляем в конец
print("\n2. Добавляем в конец (append):")
lst.append(10)
lst.append(20)
lst.append(30)
print(f"   После append: {lst}")
print(f"   Длина: {len(lst)}")          # 3

# Добавляем в начало
print("\n3. Добавляем в начало (prepend):")
lst.prepend(5)
print(f"   После prepend(5): {lst}")

# Вставляем по индексу
print("\n4. Вставляем по индексу (insert):")
lst.insert(2, 15)
print(f"   После insert(2, 15): {lst}")

# Проверяем итерацию
print("\n5. Проверяем цикл for:")
print("   Элементы:", end=" ")
for x in lst:
    print(x, end=" ")
print()

# Проверяем граничные случаи
print("\n6. Граничные случаи:")
lst.insert(0, 1)      # в начало
lst.insert(len(lst), 100)  # в конец
print(f"   После insert в начало и конец: {lst}")

# Проверяем ошибки
print("\n7. Проверяем ошибки:")
try:
    lst.insert(-5, 999)
except IndexError as e:
    print(f"   Ошибка при insert(-5): {e}")

try:
    lst.insert(100, 100)
except IndexError as e:
    print(f"   Ошибка при insert(100): {e}")
```

[![546456464.png](https://i.postimg.cc/hGc5BCD3/546456464.png)](https://postimg.cc/RWpR1Lnc)
