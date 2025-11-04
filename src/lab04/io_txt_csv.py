import csv
from pathlib import Path
from typing import Iterable, Sequence, Union


def read_text(path: Union[str, Path], encoding: str = "utf-8") -> str:
    """
    Читает текстовый файл и возвращает его содержимое как строку.
    
    Args:
        path: Путь к файлу
        encoding: Кодировка файла (по умолчанию UTF-8). 
                 Для русских текстов можно использовать 'cp1251', 'koi8-r'
    
    Returns:
        Содержимое файла как строка
        
    Raises:
        FileNotFoundError: Если файл не существует
        UnicodeDecodeError: Если не удается декодировать файл в указанной кодировке
    """
    p = Path(path)
    return p.read_text(encoding=encoding)


def write_csv(rows: Iterable[Sequence], path: Union[str, Path], 
              header: tuple[str, ...] = None) -> None:
    """
    Записывает данные в CSV файл.
    
    Args:
        rows: Итерируемый объект с данными для записи
        path: Путь для сохранения CSV файла
        header: Заголовок столбцов (опционально)
        
    Raises:
        ValueError: Если строки имеют разную длину
    """
    p = Path(path)
    rows_list = list(rows)
    
    # Проверка одинаковой длины строк
    if rows_list:
        first_len = len(rows_list[0])
        for i, row in enumerate(rows_list):
            if len(row) != first_len:
                raise ValueError(f"Строка {i} имеет длину {len(row)}, ожидалось {first_len}")
    
    with p.open('w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        if header is not None:
            writer.writerow(header)
        writer.writerows(rows_list)


def ensure_parent_dir(path: Union[str, Path]) -> None:
    """
    Создает родительские директории для указанного пути, если они не существуют.
    
    Args:
        path: Путь к файлу
    """
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)