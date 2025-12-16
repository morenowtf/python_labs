#!/usr/bin/env python3
"""
Тестовый скрипт для проверки лабораторной работы 9.
"""

from src.lab09.group import Group, Student

def main():
    # Создаем группу студентов
    group = Group("data/lab09/students.csv")
    
    print("Изначательный список:\n")
    for s in group.list():
        print(s)
    
    # 1. Добавление студентов (CREATE)
    print("\n1. ДОБАВЛЕНИЕ СТУДЕНТОВ (CREATE):")
    print("-" * 30)
    
    new_student = Student("Горьковой Владислав", "2006-07-23", "БИВТ-25-1", 4.2) # Создаем нового студента
    group.add(new_student) # Добавляем студентов в группу
    
    # 2. Просмотр всех студентов (READ)
    print("\n2. ВСЕ СТУДЕНТЫ (READ):")
    print("-" * 30)
    all_students = group.list()
    for i, student in enumerate(all_students, 1):
        print(f"{i}. {student}")
    
    # 3. Поиск студентов (READ - поиск)
    print("\n3. ПОИСК СТУДЕНТОВ ПО 'Котилевич' (READ - поиск):")
    print("-" * 30)
    found_students = group.find("Котилевич")
    for i, student in enumerate(found_students, 1):
        print(f"{i}. {student}")
    
    # 4. Обновление студента (UPDATE)
    print("\n4. ОБНОВЛЕНИЕ ДАННЫХ СТУДЕНТА (UPDATE):")
    print("-" * 30)
    # Улучшим успеваемость Егора
    group.update("Котилевич Егор Александрович", gpa = 2.4, group = "БИВТ-25-1")
    
    # Проверим, что обновилось
    print("\nПосле обновления:")
    all_students = group.list()
    for i, student in enumerate(all_students, 1):
        print(f"{i}. {student}")
    
    # 5. Удаление студента (DELETE)
    print("\n5. УДАЛЕНИЕ СТУДЕНТА ВЛАДИКА(DELETE):")
    print("-" * 30)
    group.remove("Горьковой Владислав")
    
    # Проверим, что удалилось
    print("\nПосле удаления:")
    all_students = group.list()
    for i, student in enumerate(all_students, 1):
        print(f"{i}. {student}")
    
    
    print("\n" + "=" * 25)
    print("ТЕСТИРОВАНИЕ ЗАВЕРШЕНО!")
    print("=" * 25)
    
    # Показать содержимое CSV файла
    print("\nСОДЕРЖИМОЕ CSV ФАЙЛА:")
    print("-" * 30)
    with open("data/lab09/students.csv", "r", encoding="utf-8") as f:
        print(f.read())

if __name__ == "__main__":
    main()