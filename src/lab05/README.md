# Лабораторная работа 5

## Задание А

``` python 
import json
import csv
from pathlib import Path


def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Преобразует JSON-файл в CSV.
    Поддерживает список словарей [{...}, {...}], заполняет отсутствующие поля пустыми строками.
    """
    json_path = Path(json_path)
    csv_path = Path(csv_path)
    
    if not json_path.exists():
        raise FileNotFoundError(f"JSON файл не найден: {json_path}")
    
    # Чтение JSON
    try:
        with json_path.open('r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        raise ValueError(f"Ошибка декодирования JSON: {e}")
    
    # Валидация данных
    if not data:
        raise ValueError("Пустой JSON или неподдерживаемая структура")
    
    if not isinstance(data, list):
        raise ValueError("JSON должен содержать список объектов")
    
    if not all(isinstance(item, dict) for item in data):
        raise ValueError("Все элементы JSON должны быть словарями")
    
    if not data:
        raise ValueError("Пустой список в JSON")
    
    # Определение всех возможных полей (алфавитный порядок)
    all_fields = set()
    for item in data:
        all_fields.update(item.keys())
    fieldnames = sorted(all_fields)
    
    # Если есть данные, используем порядок из первого элемента + остальные поля
    if data and data[0]:
        first_item_fields = list(data[0].keys())
        additional_fields = sorted(all_fields - set(first_item_fields))
        fieldnames = first_item_fields + additional_fields
    
    # Запись CSV
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    
    with csv_path.open('w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        
        for item in data:
            # Заполняем отсутствующие поля пустыми строками
            row = {field: item.get(field, '') for field in fieldnames}
            writer.writerow(row)


def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Преобразует CSV в JSON (список словарей).
    Заголовок обязателен, значения сохраняются как строки.
    """
    csv_path = Path(csv_path)
    json_path = Path(json_path)
    
    if not csv_path.exists():
        raise FileNotFoundError(f"CSV файл не найден: {csv_path}")
    
    # Чтение CSV
    rows = []
    try:
        with csv_path.open('r', encoding='utf-8') as f:
            # Автоопределение разделителя
            sample = f.read(1024)
            f.seek(0)
            sniffer = csv.Sniffer()
            dialect = sniffer.sniff(sample)
            
            reader = csv.DictReader(f, dialect=dialect)
            
            for row in reader:
                rows.append(row)
                
    except csv.Error as e:
        raise ValueError(f"Ошибка чтения CSV: {e}")
    except Exception as e:
        raise ValueError(f"Ошибка обработки CSV: {e}")
    
    # Валидация
    if not rows:
        raise ValueError("CSV файл пуст или содержит только заголовок")
    
    # Запись JSON
    json_path.parent.mkdir(parents=True, exist_ok=True)
    
    with json_path.open('w', encoding='utf-8') as f:
        json.dump(rows, f, ensure_ascii=False, indent=2)
```
![Картинка 1](./images/lab05/json_csv.png)
![Картинка 2](./images/lab05/people_json_csv.png)
![Картинка 3](./images/lab05/students_recipes_json_csv.png)

## Задание В

``` python
import csv
from pathlib import Path
from openpyxl import Workbook
from openpyxl.utils import get_column_letter


def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """
    Конвертирует CSV в XLSX.
    Использовать openpyxl.
    Первая строка CSV — заголовок.
    Лист называется "Sheet1".
    Колонки — автоширина по длине текста (не менее 8 символов).
    """
    csv_path = Path(csv_path)
    xlsx_path = Path(xlsx_path)
    
    if not csv_path.exists():
        raise FileNotFoundError(f"CSV файл не найден: {csv_path}")
    
    # Чтение CSV
    data = []
    try:
        with csv_path.open('r', encoding='utf-8') as f:
            # Автоопределение разделителя
            sample = f.read(1024)
            f.seek(0)
            sniffer = csv.Sniffer()
            dialect = sniffer.sniff(sample)
            
            reader = csv.reader(f, dialect=dialect)
            
            for row in reader:
                data.append(row)
                
    except csv.Error as e:
        raise ValueError(f"Ошибка чтения CSV: {e}")
    except Exception as e:
        raise ValueError(f"Ошибка обработки CSV: {e}")
    
    # Валидация
    if not data:
        raise ValueError("CSV файл пуст")
    
    # Создание XLSX
    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"
    
    # Запись данных
    for row in data:
        ws.append(row)
    
    # Настройка автоширины колонок
    for col_idx, column_cells in enumerate(ws.columns, 1):
        max_length = 0
        column_letter = get_column_letter(col_idx)
        
        for cell in column_cells:
            try:
                if cell.value:
                    max_length = max(max_length, len(str(cell.value)))
            except:
                pass
        
        # Минимальная ширина 8 символов
        adjusted_width = max(max_length + 2, 8)
        ws.column_dimensions[column_letter].width = adjusted_width
    
    # Сохранение
    xlsx_path.parent.mkdir(parents=True, exist_ok=True)
    wb.save(xlsx_path)
```

![Картинка 4](./images/lab05/csv_xslx.png)
![Картинка 5](./images/lab05/cities_csv_xslx.png)
![Картинка 6](./images/lab05/weather_csv_xslx.png)
