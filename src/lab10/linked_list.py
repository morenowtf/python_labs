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