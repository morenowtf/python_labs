from dataclasses import dataclass, asdict  # dataclass - для удобных классов
from datetime import datetime, date        # datetime - для работы с датами
import re                                  # re - для проверки форматов (регулярные выражения)


@dataclass
class Student:
    """
    Класс Student представляет студента.
    
    Поля (атрибуты):
    - fio: ФИО студента (строка)
    - birthdate: Дата рождения в формате ГГГГ-ММ-ДД (строка)
    - group: Группа студента (строка)
    - gpa: Средний балл от 0 до 5 (число с плавающей точкой)
    """
    
    fio: str
    birthdate: str
    group: str
    gpa: float

    def __post_init__(self):
        """
        Метод, который автоматически вызывается после создания объекта (после __init__).
        Здесь мы проверяем, что данные корректные (валидация).
        """
        
        # TODO: добавить нормальную валидацию формата даты и диапазона gpa
        # ВАЛИДАЦИЯ 1: Проверяем формат даты рождения
        try:
            # Пытаемся разобрать строку с датой в нужном формате
            datetime.strptime(self.birthdate, "%Y-%m-%d")
        except ValueError:
            # (по-хорошему, тут должен быть raise ValueError(...))
            print("warning: birthdate format might be invalid")
        
        # ВАЛИДАЦИЯ 3: Проверяем, что GPA в диапазоне от 0 до 5
        if not (0 <= self.gpa <= 5):
            raise ValueError("gpa must be between 0 and 5")

    def age(self) -> int:
        """
        Вычисляет возраст студента в полных годах.
        
        Возвращает:
            int: количество полных лет
        """
        # TODO: добавить нормальную валидацию формата даты и диапазона gpa
        
        """b = dself.birthdate
        today = date.today()
        return today.year - b.year"""
    
    
        # Преобразуем строку с датой рождения в объект datetime
        birth_date = datetime.strptime(self.birthdate, "%Y-%m-%d").date()
        
        # Получаем сегодняшнюю дату
        today = date.today()
        
        # Вычисляем разницу в годах
        age_years = today.year - birth_date.year
        
        # Проверяем, был ли уже день рождения в этом году
        # Сравниваем месяц и день (не учитывая год)
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age_years -= 1  # Если день рождения еще не был, вычитаем 1 год
        
        return age_years

    def to_dict(self) -> dict:
        """
        Преобразует объект Student в словарь (для сохранения в JSON).
        
        Возвращает:
            dict: словарь с данными студента
        """
        # TODO: проверить полноценность полей
        
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa
        }

    @classmethod
    def from_dict(cls, data: dict):
        """
        Создает объект Student из словаря.
        
        Аргументы:
            data (dict): словарь с данными студента
        
        Возвращает:
            Student: новый объект Student
        """
        # TODO: реализовать десереализацию из словаря
        # cls - это сам класс Student
        # Мы просто передаем данные из словаря в конструктор класса
        return cls(
            fio=data["fio"],
            birthdate=data["birthdate"],
            group=data["group"],
            gpa=data["gpa"]
        )

    def __str__(self):
        """
        Возвращает строковое представление студента.
        Вызывается при использовании print() или str().
        
        Возвращает:
            str: красиво отформатированная строка
        """
        # TODO: f"{}, {}, {}"
        
        
        return (f"Студент: {self.fio}\n"
                f"Дата рождения: {self.birthdate}\n"
                f"Группа: {self.group}\n"
                f"Средний балл (GPA): {self.gpa}")
        
        
if __name__ == "__main__":
    student = Student("Королева Дарья Михайловна", "2006-09-26", "БИВТ-25-1", 5.0)
    print(student)
    print( "=" * 140)

    print(f"Возраст: {student.age()}")
    
    student_dict = student.to_dict()
    print(f"Сериализованный: {student_dict}")
    
    restored_student = Student.from_dict(student_dict)
    print(f"Десериализованный: {restored_student}")