# python_labs
# Лабораторная работа 4
## Задание A (io_txt_csv.py)
```python
# read_text / write_csv (+ ensure_parent_dir)
import csv
from pathlib import Path
from typing import Iterable, Sequence
from collections import Counter
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from lib.text import normalize, tokenize, count_freq, top_n


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """Читает текстовый файл и возвращает его содержимое в виде строки.
    
    Аргументы:
    path: Путь к файлу (строка или Path-объект)
    encoding: Кодировка файла
    
    Возвращает:
    Содержимое файла как строку"""
        
    p = Path(path)
    # FileNotFoundError и UnicodeDecodeError пусть «всплывают» — это нормально
    return p.read_text(encoding=encoding)

def write_csv(rows: Iterable[Sequence], path: str | Path,
              header: tuple[str, ...] | None = None) -> None:
    """Записывает данные в CSV-файл, создавая при необходимости родительские директории.
    
    Аргументы:
    rows: Итерируемый объект со строками данных
    path: Путь для сохранения CSV-файла
    header: Опциональный заголовок для CSV
    """
    p = Path(path)
    rows = list(rows)
    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header) # Записываем заголовок если он предоставлен
        for r in rows:
            w.writerow(r) # Записываем каждую строку данных

def frequencies_from_text(text: str) -> dict[str, int]:
    """Вычисляет частоты слов в тексте после нормализации и токенизации.
    Принимает - text: Исходный текст для анализа | Возвращает - Словарь с частотой каждого слова"""

    tokens = tokenize(normalize(text)) # Нормализация -> токенизация
    return Counter(tokens)  # Подсчет частот с помощью Counter

def sorted_word_counts(freq: dict[str, int]) -> list[tuple[str, int]]:
    """Сортирует словарь частот по убыванию частоты и лексикографически.
    Принимает - freq: Словарь с частотами слов | Возвращает - Отсортированный список кортежей (слово, частота)"""
    
    # Сортировка сначала по убыванию частоты (-kv[1]), 
    # затем по алфавиту (kv[0])
    return sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))
```
Этот скрипт предоставляет функции для чтения текстовых файлов, анализа частотности слов и записи результатов в CSV-файл с автоматическим созданием директорий.


## Задание B (text_report.py)

```python
import sys
import os
from pathlib import Path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from lab04.io_txt_csv import read_text, write_csv, sorted_word_counts, frequencies_from_text
from lib.text import summary  # Импорт функции для анализа текста

def main():
    # Читаем текстовый файл, анализируем его содержимое и генерируем CSV-отчет с частотой слов
    
    # Парсим аргументы командной строки: входной файл и его кодировку
    parser = argparse.ArgumentParser(description='Generate word frequency report')
    parser.add_argument('--in', dest='input_file', default='./data/lab04/input.txt',
                       help='Input text file path')
    parser.add_argument('--encoding', default='utf-8',
                       help='Input file encoding (default: utf-8)')
    args = parser.parse_args()

    try:        
         # Чтение содержимого текстового файла с использованием указанных пути и кодировки
        content = read_text(args.input_file, encoding=args.encoding)
        
        # Проверка, не пустой ли файл
        if not content.strip():
            print("Файл пуст")
            # Создание пустого CSV-файла с заголовками
            write_csv([], "./data/lab04/report.csv", header=("word", "count"))
        else:
            # Вывод статистической сводки по тексту
            print(summary(content))
            
            # Создание CSV-отчета с отсортированными частотами слов:
            # 1. frequencies_from_text - подсчет частоты слов
            # 2. sorted_word_counts - сортировка слов по частоте
            # 3. write_csv - запись результатов в CSV-файл
            content = write_csv(
                sorted_word_counts(frequencies_from_text(content)),
                "./data/lab04/report.csv", 
                header=("word", "count")
            )

    # Обработка различных типов исключений
    except FileNotFoundError as e:
        print(f"Ошибка: Файл не найден - {e}")
    except UnicodeDecodeError:
        print("Ошибка: Проблема с кодировкой файла!")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

# Точка входа в программу
if __name__ == "__main__":
    main()
```
Этот скрипт анализирует текстовый файл, подсчитывает частоту слов и сохраняет отсортированные результаты в CSV-файл с обработкой ошибок.

## Тест-кейсы
### Тест-кейс A

Пишем текст на вход в файле (data/input.txt):
```
Привет, мир! Привет!!!
```

Вводим в терминал команду "python src/lab04/text_report.py --in data/lab04/input.txt --out data/lab04/report.csv"

В консоле получаем:

[![501.png](https://i.postimg.cc/rpNbFzPM/501.png)](https://postimg.cc/1g4MvRSj)

А в папке data/lab04 создаётся файл "report.csv" с такими данными:

[![502.png](https://i.postimg.cc/Fs0wnPg2/502.png)](https://postimg.cc/HVsSr9N2)

### Тест-кейс B

Не пишем текст на вход в файле, оставляем его пустым (data/input.txt)

Вводим в терминал команду "python src/lab04/text_report.py --in data/lab04/input.txt --out data/lab04/report.csv"

В консоле получаем:

[![503.png](https://i.postimg.cc/3xdmxqf7/503.png)](https://postimg.cc/fVQJH8hg)

А в самом файле получаем:

[![504.png](https://i.postimg.cc/rsZz6Vkd/504.png)](https://postimg.cc/PvZdYkNh)

### Тест-кейс C

Пишем на вход в файле (data/input.txt) слово "Привет", а так же меняем кодировку файла с utf8 на cp1251:

Вводим в терминал команду "python src/lab04/text_report.py --in data/lab04/input.txt --encoding cp1251"

В файле "report.csv" получаем:

[![505.png](https://i.postimg.cc/QC6L0Vrw/505.png)](https://postimg.cc/BP1wvSbB)


