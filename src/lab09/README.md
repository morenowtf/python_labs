# Лабораторная работа 9

## Group.py

``` python 
import csv
from pathlib import Path
from src.lab08.models import Student

from typing import List

class Group:
    # Класс для управления студентами в CSV-файле. Реализует CRUD-операции: Create, Read, Update, Delete
    
    def __init__(self, storage_path: str):
        # Инициализация группы студентов

        self.path = Path(storage_path)
        if not self.path.exists():
            self.path.write_text("fio,birthdate,group,gpa\n", encoding="utf-8")  # Записать заголовок 

    def _read_all(self):
        # Читаем все записи из CSV-файла и возвращает список словарей

        students = []
        try:
            with open(self.path, 'r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    students.append(row)
        except FileNotFoundError:
            # Если файл не найден, возвращаем пустой список
            pass
        return students

    def _write_all(self, students: List[dict]):
        # Записываем всех студентов в CSV-файл

        with open(self.path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['fio', 'birthdate', 'group', 'gpa'])
            writer.writeheader()
            writer.writerows(students)

    def list(self):
        # Получаем всех студентов
        
        students_data = self._read_all()
        students = []
        for data in students_data:
            # Преобразуем GPA в число с плавающей точкой
            gpa = float(data['gpa'])
            student = Student(
                fio=data['fio'],
                birthdate=data['birthdate'],
                group=data['group'],
                gpa=gpa
            )
            students.append(student)
        return students

    def add(self, student: Student):
        # Добавляем нового студента

        # Читаем существующих студентов
        students = self._read_all()
        
        # Добавляем нового студента
        new_student = {
            'fio': student.fio,
            'birthdate': student.birthdate,
            'group': student.group,
            'gpa': str(student.gpa)  # Преобразуем в строку для CSV
        }
        
        students.append(new_student)
        
        # Записываем обратно в файл
        self._write_all(students)
        print(f"Студент '{student.fio}' успешно добавлен!")
        return True 
         

    def find(self, substr: str):
        # Найти студентов по подстроке в ФИО

        all_students = self.list()
        found_students = []
        
        for student in all_students:
            if substr.lower() in student.fio.lower():
                found_students.append(student)
        
        return found_students

    def remove(self, fio: str):
        # Удалить студента по ФИО
        
        students = self._read_all()
        initial_count = len(students)
        
        # Фильтруем студентов, оставляя только тех, у кого не совпадает ФИО
        students = [s for s in students if s['fio'] != fio]
        
        if len(students) < initial_count:
            self._write_all(students)
            print(f"Студент '{fio}' успешно удален!")
            return True
        else:
            print(f"Студент с ФИО '{fio}' не найден!")
            return False
        
        
    def update(self, fio: str, **fields):
        # Обновить данные студента

        students = self._read_all()
        updated = False
        
        for student in students:
            if student['fio'] == fio:
                # Обновляем указанные поля
                for field, value in fields.items():
                    if field in student:
                        student[field] = str(value)
                        updated = True
                
                if updated:
                    self._write_all(students)
                    print(f"Данные студента '{fio}' успешно обновлены!")
                    return True
        
        print(f"Студент с ФИО '{fio}' не найден!")
        return False
```

Этот код позволяет управлять списком студентов через CSV-файл - добавлять новых, удалять, искать и обновлять их данные, как в простой базе данных.

## Тест (test_lab09.py)

``` python
from src.lab09.group import Group, Student

def main():
    # Создаем группу студентов
    group = Group("data/lab09/students.csv")
    
    print("Изначальный список:\n")
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
```

[![8768686784.png](https://i.postimg.cc/4yQTPCnJ/8768686784.png)](https://postimg.cc/m1kqZ5Qq)

[![7887867868.png](https://i.postimg.cc/DyhvX6mV/7887867868.png)](https://postimg.cc/23HNp44T)
[![867868686.png](https://i.postimg.cc/nc1HYmQg/867868686.png)](https://postimg.cc/LnnKmnD3)
