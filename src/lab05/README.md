# Лабораторная работа 5

## Задание А

``` python 
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
```

Этот код содержит две функции для конвертации между JSON и CSV форматами: json_to_csv преобразует JSON-файл в CSV, а csv_to_json выполняет обратное преобразование.
[![41.png](https://i.postimg.cc/Rh59fj8G/41.png)](https://postimg.cc/8JHqgnTr)
[![42.png](https://i.postimg.cc/4xNGzv8L/42.png)](https://postimg.cc/jL9BTfYP)

## Задание В

``` python
import csv
from pathlib import Path
from openpyxl import Workbook
from openpyxl.utils import get_column_letter


def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """
    Преобразует CSV файл в формат XLSX.
    Используется библиотека openpyxl для работы с Excel.
    Первая строка исходного файла считается заголовком таблицы.
    Лист получает название "Sheet1".
    Для удобства просмотра устанавливается автоширина колонок с минимальным значением 8 символов.
    """
    # Преобразуем пути в объекты Path для удобной работы с файловой системой
    csv_file = Path(csv_path)
    excel_file = Path(xlsx_path)
    
    # Проверяем существование исходного CSV файла
    if not csv_file.exists():
        raise FileNotFoundError(f"Не удается найти CSV файл по указанному пути: {csv_file}")
    
    # Читаем данные из CSV файла
    csv_data = []
    try:
        # Открываем файл с автоматическим определением кодировки
        with csv_file.open('r', encoding='utf-8') as file:
            # Определяем разделитель по содержимому файла
            sample_content = file.read(1024)
            file.seek(0)  # Возвращаемся к началу файла
            dialect_detector = csv.Sniffer()
            csv_dialect = dialect_detector.sniff(sample_content)
            
            # Создаем reader с определенным разделителем
            csv_reader = csv.reader(file, dialect=csv_dialect)
            
            # Построчно считываем все данные
            for line in csv_reader:
                csv_data.append(line)
                
    except csv.Error as e:
        raise ValueError(f"Проблема с форматом CSV файла: {e}")
    except Exception as e:
        raise ValueError(f"Общая ошибка при обработке CSV: {e}")
    
    # Проверяем что файл не пустой
    if not csv_data:
        raise ValueError("CSV файл не содержит данных")
    
    # Создаем новую книгу Excel
    excel_workbook = Workbook()
    excel_sheet = excel_workbook.active
    excel_sheet.title = "Sheet1"  # Устанавливаем название листа
    
    # Переносим данные из CSV в Excel
    for row_data in csv_data:
        excel_sheet.append(row_data)
    
    # Настраиваем ширину колонок для лучшего отображения
    for column_index, column_cells in enumerate(excel_sheet.columns, 1):
        max_text_length = 0
        current_column_letter = get_column_letter(column_index)
        
        # Ищем самую длинную ячейку в колонке
        for cell in column_cells:
            try:
                if cell.value is not None:
                    # Обновляем максимальную длину если нашли большее значение
                    max_text_length = max(max_text_length, len(str(cell.value)))
            except:
                # Пропускаем ячейки с ошибками преобразования
                continue
        
        # Устанавливаем ширину колонки (минимум 8 символов)
        column_width = max(max_text_length + 2, 8)
        excel_sheet.column_dimensions[current_column_letter].width = column_width
    
    # Сохраняем результат
    excel_file.parent.mkdir(parents=True, exist_ok=True)  # Создаем папки если нужно
    excel_workbook.save(excel_file)
```

Этот код конвертирует CSV-файл в XLSX-формат с автоматической настройкой ширины колонок.
[![43.png](https://i.postimg.cc/FHBRWFBQ/43.png)](https://postimg.cc/87LNsGGy)
[![44.png](https://i.postimg.cc/xCK11vjx/44.png)](https://postimg.cc/9RQhxq7Z)
