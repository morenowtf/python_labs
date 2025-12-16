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