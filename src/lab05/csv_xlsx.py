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