import csv
from pathlib import Path
from src.lab08.models import Student

from typing import List
from datetime import datetime

class Group:
    """
    Класс для управления студентами в CSV-файле.
    Реализует CRUD-операции: Create, Read, Update, Delete.
    """
    
    def __init__(self, storage_path: str):
        """
        Инициализация группы студентов.
        
        Args:
            storage_path (str): Путь к CSV-файлу с данными студентов
        """
        self.path = Path(storage_path)
        if not self.path.exists():
            self.path.write_text("fio,birthdate,group,gpa\n", encoding="utf-8")  # Записать заголовок 

    def _read_all(self):
        """
        Вспомогательный метод.
        Читает все записи из CSV-файла и возвращает список словарей.
        
        Returns:
            List[dict]: Список студентов в виде словарей
        """
        # TODO: реализовать чтение строк из csv 
        
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
        """
        Вспомогательный метод.
        Записывает всех студентов в CSV-файл.
        
        Args:
            students (List[dict]): Список студентов для записи
        """
        with open(self.path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['fio', 'birthdate', 'group', 'gpa'])
            writer.writeheader()
            writer.writerows(students)

    def list(self):
        """
        Получить всех студентов.
        
        Returns:
            List[Student]: Список объектов Student
        """
        # TODO: реализовать метод list()
        
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
        """
        Добавить нового студента.
        
        Args:
            student (Student): Объект студента для добавления
        """
         # TODO: реализовать метод add()
         
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
        """
        Найти студентов по подстроке в ФИО.
        
        Args:
            substr (str): Подстрока для поиска в ФИО
            
        Returns:
            List[Student]: Список найденных студентов
        """
        # TODO: реализовать метод find()
        all_students = self.list()
        found_students = []
        
        for student in all_students:
            if substr.lower() in student.fio.lower():
                found_students.append(student)
        
        return found_students

    def remove(self, fio: str):
        """
        Удалить студента по ФИО.
        
        Args:
            fio (str): ФИО студента для удаления
            
        Returns:
            bool: True если студент удален, False если не найден
        """
        # TODO: реализовать метод remove()
        
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
        """
        Обновить данные студента.
        
        Args:
            fio (str): ФИО студента для обновления
            **fields: Поля для обновления (например: birthdate='2004-01-01', gpa=5.0)
        
        Returns:
            bool: True если обновлено успешно, False если студент не найден
        """
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