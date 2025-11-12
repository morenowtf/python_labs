import json
import csv
from pathlib import Path


def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Конвертирует данные из JSON формата в CSV.
    Работает с массивами объектов [{...}, {...}], автоматически заполняет пропущенные поля.
    Отлично подходит для экспорта данных из веб-API в табличный формат.
    """
    json_file = Path(json_path)
    csv_file = Path(csv_path)
    
    # Проверка существования исходного файла - важно для избежания ошибок
    if not json_file.exists():
        raise FileNotFoundError(f"Не могу найти JSON файл: {json_file}")
    
    # Загружаем и парсим JSON данные
    try:
        with json_file.open('r', encoding='utf-8') as file:
            json_data = json.load(file)
    except json.JSONDecodeError as e:
        raise ValueError(f"Некорректный JSON формат: {e}")
    
    # Проверяем что данные вообще есть и они в нужном формате
    if not json_data:
        raise ValueError("JSON файл пустой или содержит невалидные данные")
    
    # Убеждаемся что это именно список объектов
    if not isinstance(json_data, list):
        raise ValueError("JSON должен быть массивом объектов")
    
    # Проверяем что все элементы - словари (объекты в терминах JSON)
    if not all(isinstance(record, dict) for record in json_data):
        raise ValueError("Все элементы массива должны быть объектами")
    
    if not json_data:
        raise ValueError("Массив в JSON пустой")
    
    # Собираем все возможные названия полей из всех объектов
    # Используем set чтобы автоматически убрать дубликаты
    all_columns = set()
    for record in json_data:
        all_columns.update(record.keys())
    
    # Сортируем поля для единообразия, но стараемся сохранить порядок из первого элемента
    sorted_columns = sorted(all_columns)
    
    # Хитрый момент: если в данных есть первый элемент, используем порядок его полей как основной
    # Остальные поля добавляем в конце в алфавитном порядке
    if json_data and json_data[0]:
        first_record_fields = list(json_data[0].keys())
        extra_fields = sorted(all_columns - set(first_record_fields))
        sorted_columns = first_record_fields + extra_fields
    
    # Создаем папку для результата если её нет
    csv_file.parent.mkdir(parents=True, exist_ok=True)
    
    # Записываем данные в CSV формате
    with csv_file.open('w', newline='', encoding='utf-8') as file:
        csv_writer = csv.DictWriter(file, fieldnames=sorted_columns)
        csv_writer.writeheader()  # Записываем строку с названиями колонок
        
        # Проходим по всем записям и формируем строки
        for record in json_data:
            # Для каждой записи создаем строку, заполняя отсутствующие поля пустыми значениями
            csv_row = {column: record.get(column, '') for column in sorted_columns}
            csv_writer.writerow(csv_row)


def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Преобразует CSV файл в JSON массив объектов.
    Первая строка CSV используется как заголовок для названий полей.
    Все значения сохраняются как строки - это особенность формата CSV.
    """
    csv_file = Path(csv_path)
    json_file = Path(json_path)
    
    # Всегда проверяем что исходный файл существует
    if not csv_file.exists():
        raise FileNotFoundError(f"CSV файл отсутствует: {csv_file}")
    
    # Читаем данные из CSV
    csv_records = []
    try:
        with csv_file.open('r', encoding='utf-8') as file:
            # Умное определение разделителя - запятая, точка с запятой, табуляция и т.д.
            file_sample = file.read(1024)
            file.seek(0)  # Возвращаемся в начало файла
            csv_dialect_detector = csv.Sniffer()
            csv_dialect = csv_dialect_detector.sniff(file_sample)
            
            # Используем DictReader чтобы автоматически использовать заголовки как ключи
            csv_reader = csv.DictReader(file, dialect=csv_dialect)
            
            # Построчно читаем все данные в память
            for data_row in csv_reader:
                csv_records.append(data_row)
                
    except csv.Error as e:
        raise ValueError(f"Проблема с чтением CSV: {e}")
    except Exception as e:
        raise ValueError(f"Неожиданная ошибка при обработке CSV: {e}")
    
    # Проверяем что в файле есть данные кроме заголовка
    if not csv_records:
        raise ValueError("CSV файл не содержит данных или имеет только заголовки")
    
    # Создаем необходимые директории для выходного файла
    json_file.parent.mkdir(parents=True, exist_ok=True)
    
    # Сохраняем данные в JSON формате с красивым форматированием
    with json_file.open('w', encoding='utf-8') as file:
        json.dump(csv_records, file, ensure_ascii=False, indent=2)