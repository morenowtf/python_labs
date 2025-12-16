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
print("=== Тест Queue ===")
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

# Тест SinglyLinkedList
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