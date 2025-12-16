# Лабораторная работа 8

## 1. Models.py

``` python 
from dataclasses import dataclass
from datetime import datetime, date


@dataclass
class Student:
    
    fio: str
    birthdate: str
    group: str
    gpa: float

    def __post_init__(self):
        # ВАЛИДАЦИЯ 1: Проверяем формат даты рождения
        try:
            # Пытаемся разобрать строку с датой в нужном формате
            datetime.strptime(self.birthdate, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Warning: birthdate format might be invalid")
        
        # ВАЛИДАЦИЯ 2: Проверяем, что GPA в диапазоне от 0 до 5
        if not (0 <= self.gpa <= 5):
            raise ValueError("Gpa must be between 0 and 5")

    def age(self) -> int:
        # Преобразуем строку с датой рождения в объект datetime
        birth_date = datetime.strptime(self.birthdate, "%Y-%m-%d").date()
        
        # Получаем сегодняшнюю дату
        today = date.today()
        
        # Вычисляем разницу в годах
        age_years = today.year - birth_date.year
        
        # Проверяем, был ли уже день рождения в этом году, сравниваем месяц и день (не учитывая год)
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age_years -= 1  # Если день рождения еще не был, вычитаем 1 год
        
        return age_years

    def to_dict(self) -> dict:
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa
        }

    @classmethod
    def from_dict(cls, data: dict):
        # cls - это сам класс Student. Мы просто передаем данные из словаря в конструктор класса
        return cls(
            fio=data["fio"],
            birthdate=data["birthdate"],
            group=data["group"],
            gpa=data["gpa"]
        )

    def __str__(self):
        return (f"Студент: {self.fio}\n"
                f"Дата рождения: {self.birthdate}\n"
                f"Группа: {self.group}\n"
                f"Средний балл (GPA): {self.gpa}")
```

Этот код создаёт удобный класс Student для хранения данных о студенте с проверкой корректности даты рождения и среднего балла, а также методами для вычисления возраста и преобразования в словарь.

## Тест

``` python
if __name__ == "__main__":
    student = Student("Котилевич Егор Александрович", "2006-10-27", "БИВТ-25-1", 2.1)
    print(student)
    print( "=" * 35)

    print(f"Возраст: {student.age()}")
    
    student_dict = student.to_dict()
    print(f"Сериализованный: {student_dict}")
    
    restored_student = Student.from_dict(student_dict)
    print(f"Десериализованный: {restored_student}")
```

[![9789797897.png](https://i.postimg.cc/65kkDpJj/9789797897.png)](https://postimg.cc/VdFZt1Nn)

## 2. Serialize.py

``` python
# imports
import json
from models import Student

def students_to_json(students: list[Student], path: str) -> None:
    """
        students: список объектов Student
        path: путь к файлу для сохранения
    """
    students_data = [student.to_dict() for student in students]
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(students_data, f, ensure_ascii=False, indent=2)


def students_from_json(path: str) -> list[Student]:
    """
        path: путь к JSON файлу
        list[Student]: список объектов Student
    """
    try:
        with open(path, 'r', encoding='utf-8') as f:
            students_data = json.load(f)
   
        students = [Student.from_dict(data) for data in students_data]
        return students
    except FileNotFoundError:
        print(f"Файл {path} не найден")
        return []
```

Этот код сохраняет список объектов студентов в JSON-файл и загружает их обратно, проверяя работу сериализации на тестовых данных.

## Тест

``` python
def test_serialization():
    students = students_from_json('data/lab08/students_input.json')
    print("\n Загруженные студенты:")
    for student in students:
        print(f"ФИО: {student.fio}, birthdate: {student.birthdate}, group: {student.group}, GPA: {student.gpa}")
    print("\n Сохранение в выходной файл")
    students_to_json(students, 'data/lab08/students_output.json')
    print("Файл сохранен: data/lab08/students_output.json")

if __name__ == "__main__":
    test_serialization()
```

[![97898797.png](https://i.postimg.cc/wxPZmjvH/97898797.png)](https://postimg.cc/QVQfLs1n)
[![87686867867.png](https://i.postimg.cc/9Mk8ZLWj/87686867867.png)](https://postimg.cc/XGwk0cG2)
