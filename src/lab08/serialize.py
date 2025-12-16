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