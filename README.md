# Лабораторная работа 1
### Задание 1
```python
name = input("Введите ваше имя: ")
age = int(input("Введите ваш возраст: "))

print(f"Привет, {name}! Через год тебе будет {age + 1}.")
```
Считываем дни, считываем возраст, затем вывод эту информацию, предватирительно прибавив один год к возрасту

[![img1.png](https://i.postimg.cc/DmkF39QK/img1.png)](https://postimg.cc/0KfhpHHt)

### Задание 2
```python
firstNumber = input("Введите первое число: ").replace(",", ".")
secondNumber = input("Введите второе число: ").replace(',', '.')

summary = float(firstNumber) + float(secondNumber)
avg = (summary / 2 )

print(f"Сумма = {summary} ; Среднее арифметическое = {avg}")
```
[![img2.png](https://i.postimg.cc/PxT292vF/img2.png)](https://postimg.cc/jW3HJ6Xz)

### Задание 3
```python
price = float(input("Введите цену: "))
discount = float(input("Введите процент скидки: "))
vat = float(input("Введите процент налогов: "))

base = price * (1 - discount / 100)
vat_amount = base * (vat/100)
total = base + vat_amount

print(f"База после скидки: {base:.2f} ₽ \nНДС: {vat_amount:.2f} ₽ \nИтого к оплате: {total:.2f} ₽")
```
[![img3.png](https://i.postimg.cc/yYMh2vwX/img3.png)](https://postimg.cc/LnVZ1B4n)

### Задание 4
```python
minutes = int(input("Введите минуты: "))

hours = minutes // 60
remaining_minutes = minutes % 60

print(f"Минуты: {minutes} \n{hours}:{remaining_minutes:02d}")
```
[![img44.png](https://i.postimg.cc/xC5KjjHy/img44.png)](https://postimg.cc/1nggJQvf)

### Задание 5
```python
fullName = input("Введите ФИО: ")

uppercase = ""
for char in fullName:
    if char.isupper():
        uppercase += char

strLength = len(fullName.replace(" ", ""))

print(f"Инициалы: {uppercase} \nКоличество символов без пробелов: {strLength}")
```
[![img5.png](https://i.postimg.cc/WpDXKFdV/img5.png)](https://postimg.cc/RqB7J01p)

# Лабораторная работа 2
## Задание 1
### Первая функция
```python
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if not nums:
        raise ValueError("Вы не ввели число!")

    min_number = min(nums)
    max_number = max(nums)

    return (min_number, max_number)
```
Находим минимум и максимум в списке чисел и возвращаем их как кортеж, а если список пуст - вызываем ошибку.

[![101.png](https://i.postimg.cc/TYjXyxtY/101.png)](https://postimg.cc/4m30MDCr)

### Вторая функция
```python
def unique_sorted(nums: list[float | int]) -> list[float | int]:
    unique_nums = list(set(nums))
    unique_nums.sort()
    return unique_nums

    if not nums:
        raise ValueError("Вы не ввели число!")
```
Преобразуем список в множество чтобы убрать дубликаты, затем обратно в список и сортируем по возрастанию.

[![102.png](https://i.postimg.cc/bN0jGPmd/102.png)](https://postimg.cc/bsv5M7cj)

### Третья функция
```python
def flatten(mat: list[list | tuple]) -> list:
    flattened_list = []
    for item in mat:
        if isinstance(item, (list, tuple)):
            flattened_list.extend(item) 
        else:
            raise TypeError("Строка не строка строк матрицы")
    return flattened_list
```
Проходим по всем элементам входного списка, проверяем что каждый элемент является списком или кортежем, и если да - добавляем его элементы в результирующий список, иначе выдаём ошибку.

[![103.png](https://i.postimg.cc/Nf8wytd2/103.png)](https://postimg.cc/1fzdTkhy)

## Задание 2
### Первая функция
```python
def transpose(mat: list[list[float | int]]) -> list[list]:
    if not mat:
        return []
    
    first_len = len(mat[0])
    for row in mat:
        if len(row) != first_len:
            raise ValueError("Рваная матрица")
    
    return [[mat[i][j] for i in range(len(mat))] for j in range(len(mat[0]))]
```
Меняем строки и столбцы местами, проверяя что все строки одинаковой длины.

[![201.png](https://i.postimg.cc/c47NKWFg/201.png)](https://postimg.cc/CzK2t3TS)

### Вторая функция
```python
def row_sums(mat: list[list[float | int]]) -> list[float]:
    if not mat:
        return []
    
    first_len = len(mat[0])
    for row in mat:
        if len(row) != first_len:
            raise ValueError("Рваная матрица")
    
    return [sum(row) for row in mat]
```
Суммируем элементы каждой строки, проверяя что матрица прямоугольная.

[![202.png](https://i.postimg.cc/L6kMqSxZ/202.png)](https://postimg.cc/3dwq6s5K)

### Третья функция
```python
if not mat:
        return []
    
    first_len = len(mat[0])
    for row in mat:
        if len(row) != first_len:
            raise ValueError("Рваная матрица")
    
    return [sum(mat[i][j] for i in range(len(mat))) for j in range(len(mat[0]))]
```
Суммируем элементы каждого столбца, проверяя что матрица прямоугольная.

[![203.png](https://i.postimg.cc/kgnPKHHJ/203.png)](https://postimg.cc/zVPQ1x56)

## Задание 3
```python
def format_record(rec: tuple[str, str, float]) -> str:
    fio, group, gpa = rec
    
    if not fio or not fio.strip():
        raise ValueError("ФИО не может быть пустым")
    if not group or not group.strip():
        raise ValueError("Группа не может быть пустой")
    if not isinstance(gpa, (int, float)):
        raise TypeError("GPA должно быть числом")
    
    fio_parts = ' '.join(fio.split()).title().split()
    
    if len(fio_parts) == 3:
        initials = f"{fio_parts[1][0]}.{fio_parts[2][0]}."
    elif len(fio_parts) == 2:
        initials = f"{fio_parts[1][0]}."
    else:
        raise ValueError("ФИО должно содержать 2 или 3 части")
    
    formatted_gpa = f"{gpa:.2f}"
    
    return f"{fio_parts[0]} {initials}, гр. {group.strip()}, GPA {formatted_gpa}"
```
Извлекаем ФИО, группу и GPA из кортежа, проверяем их корректность, обрабатываем ФИО для формирования инициалов, форматируем GPA до двух знаков и собираем всё в требуемую строку.

[![301.png](https://i.postimg.cc/Bbgn3MB6/301.png)](https://postimg.cc/9wDhtPS5)

# Лабораторная работа 3
## Задание A (text.py)
```python
import re

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    #Функция приводит текст к единому регистру и стилю
    s=text
    if casefold :
        s=s.casefold()
    if yo2e :
        s=s.replace("ё","е").replace("Ё","Е")
    s=s.replace("\t"," ").replace("\r"," ").replace("\n"," ")
    s = ' '.join(s.split())
    s=s.strip()

    return s

def tokenize(text: str) -> list[str]:
    #Функция разбивает текст на «слова» по небуквенно-цифровым разделителям
    pattern= r'\w+(?:-\w+)*'
    tokenstext = re.findall(pattern, text)

    return tokenstext

def count_freq(tokens: list[str]) -> dict[str, int]:
    #Функция возвращает словарь слово - количество
    counts={}
    for word in tokens:
        counts[word]=counts.get(word,0)+1
    return counts

def sort_key(item):
    return [-item[1], item[0]]

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    #Функция возвращает топ-N по убыванию частоты
    sorted_freq= sorted(freq.items(),key=sort_key)
    top_n=[]

    for i in range(min(n, len(sorted_freq))):
        top_n.append((sorted_freq[i][0], sorted_freq[i][1]))

    return top_n

def summary(text):
    normalized_text = normalize(text)

    tokens = tokenize(normalized_text)

    total_words = len(tokens)
    freq_sorted = count_freq(tokens)
    unique_words = len(freq_sorted)
    top = top_n(freq_sorted, 5)

    print(f"Всего слов: {total_words}")
    print(f"Уникальных слов: {unique_words}")
    print("Топ-5:")

    for word, count in top:
        print(f"{word}:{count}")
```
Скрипт анализирует текст, подсчитывая слова и выводя статистику по частотности.

Для теста этого скрипта, я написал второй скрипт, в котором происходит вызов этих методов (test_case.py)
```python
import sys
import os

# Добавляем корневую директорию проекта в путь поиска модулей
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, project_root)

from src.lib.text import *

print(normalize("ПрИвЕт\nМИр\t"))
print(normalize("ёжик, Ёлка", yo2e=True))
print(normalize("Hello\r\nWorld"))
print(normalize("  двойные   пробелы  "))


print(tokenize("привет мир"))
print(tokenize("hello,world!!!"))
print(tokenize("по-настоящему круто"))
print(tokenize("2025 год"))
print(tokenize("emoji 😀 не слово"))

print(top_n(count_freq(["a", "b", "a", "c", "b", "a"]), n=2))
print(top_n(count_freq(["bb", "aa", "bb", "aa", "cc"]), n=2))
```
При запуске этого скрипта, получаем вот такой результат:

[![401.png](https://i.postimg.cc/ZnJCPzsD/401.png)](https://postimg.cc/S2tSq3hW)

## Задание B (text_stats.py)

```python
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from src.lib.text import normalize, tokenize, count_freq, top_n

def main():
    # Читаем весь вход до EOF
    input_text = sys.stdin.readline()


    # Нормализация
    text_norm = normalize(input_text)
    # Токенизация
    tokens = tokenize(text_norm)
    # Подсчёт частот
    freq = count_freq(tokens)

    # Подсчёт статистики
    words_total = len(tokens)
    unique_words = len(freq)

    # Топ 5 слов
    top_words = top_n(freq, 5)

    print(f"Всего слов: {words_total}")
    print(f"Уникальных слов: {unique_words}")
    print("Топ-5:")
    for word, count in top_words:
        print(f"{word}:{count}")

if __name__ == "__main__":
    main()
```
Этот скрипт анализирует текст из stdin и выводит статистику по словам.
Запускаем этот скрипт, он ожидает ввод текста от нас, мы вводим "Привет, мир! Привет!!!", и получаем вот такой результат:

[![402.png](https://i.postimg.cc/x878wN1T/402.png)](https://postimg.cc/kRQ784Sk)

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

# Лабораторная работа 6

## Подкоманды в одном CLI

``` python 
import argparse
from pathlib import Path
from src.lib.text import tokenize, count_freq, top_n

def main():
    # Создание основного парсера аргументов командной строки
    parser = argparse.ArgumentParser(description="CLI‑утилиты лабораторной №6")
    # Добавление подпарсеров для обработки подкоманд
    subparsers = parser.add_subparsers(dest="command")

    # Парсер для подкоманды 'cat' - вывод содержимого файла
    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True, help="Путь к входному файлу")
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    # Парсер для подкоманды 'stats' - анализ частот слов
    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", required=True, help="Путь к входному файлу")
    stats_parser.add_argument("--top", type=int, default=5, help="Количество топ-слов для вывода")

    # Парсинг аргументов командной строки
    args = parser.parse_args()

    # Проверка существования файла
    file = Path(args.input)
    if not file.exists():
        raise FileNotFoundError("Файл не найден")

    # Обработка подкоманды 'cat'
    if args.command == "cat":
        # python -m src.lab06.cli_text cat --input data/samples/test.txt -n
        
        # Открытие файла для чтения
        with open(file, "r", encoding="utf-8") as f:
            num = 1  # Счетчик строк для нумерации
            # Построчное чтение файла
            for line in f:
                line = line.rstrip("\n")  # Удаление символа новой строки
                # Вывод с нумерацией или без в зависимости от флага -n
                if args.n:
                    print(f"{num}: {line}")
                    num += 1
                else:
                    print(line)

    # Обработка подкоманды 'stats'
    elif args.command == "stats":
        # python -m src.lab06.cli_text stats --input data/samples/test.txt --top 3
        
        # Чтение всего содержимого файла
        with open(file, "r", encoding="utf-8") as f:
            data = [row for row in f]  # Чтение всех строк в список
        data = "".join(data)  # Объединение строк в одну строку
    
        # Анализ текста: токенизация, подсчет частот, выбор топ-N
        tokens = tokenize(data)  # Разбивка текста на слова/токены
        freq = count_freq(tokens)  # Подсчет частоты каждого токена
        top = top_n(freq, args.top)  # Выбор N самых частых слов
    
        # Вывод результатов
        print(f"Топ-{args.top} слов в файле '{args.input}':")
        number = 1
        for word, count in top:
            print(f"{number}. '{word}' - {count} раз")
            number += 1

if __name__ == "__main__":
    main()
```

Этот код реализует CLI-утилиту с двумя командами: cat для вывода содержимого файла и stats для показа топ-N самых частых слов в файле.

[![01.png](https://i.postimg.cc/xCr9MPMc/01.png)](https://postimg.cc/gwD9P8MW)

## CLI‑конвертер

``` python
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
import argparse
from src.lab05.json_csv import json_to_csv, csv_to_json
from src.lab05.csv_xlsx import csv_to_xlsx
from pathlib import Path

def main():
    # Создаем главный парсер аргументов командной строки
    parser = argparse.ArgumentParser(description="Конвертеры данных")
    
    # Создаем субпарсер для поддержки разных команд
    sub = parser.add_subparsers(dest="cmd")

    # Парсер для конвертации JSON в CSV
    parser1 = sub.add_parser("json2csv")
    parser1.add_argument("--in", dest="input", required=True, help="Входной JSON файл")
    parser1.add_argument("--out", dest="output", required=True, help="Выходной CSV файл")

    # Парсер для конвертации CSV в JSON
    parser2 = sub.add_parser("csv2json")
    parser2.add_argument("--in", dest="input", required=True, help="Входной CSV файл")
    parser2.add_argument("--out", dest="output", required=True, help="Выходной JSON файл")

    # Парсер для конвертации CSV в XLSX
    parser3 = sub.add_parser("csv2xlsx")
    parser3.add_argument("--in", dest="input", required=True, help="Входной CSV файл")
    parser3.add_argument("--out", dest="output", required=True, help="Выходной XLSX файл")

    # Парсим аргументы командной строки
    args = parser.parse_args()

    """
        Вызываем код в зависимости от аргументов.
    """

    if args.cmd == "json2csv":
        json_to_csv(Path(args.input), Path(args.output))

    elif args.cmd == "csv2json":
        csv_to_json(Path(args.input), Path(args.output))

    elif args.cmd == "csv2xlsx":
        csv_to_xlsx(Path(args.input), Path(args.output))

if __name__ == "__main__":
    main()
```

Этот код предоставляет интерфейс командной строки для конвертации файлов между форматами JSON, CSV и XLSX.

[![02.png](https://i.postimg.cc/QxrGmtFT/02.png)](https://postimg.cc/SjVvNm7S)
[![03.png](https://i.postimg.cc/B61kc944/03.png)](https://postimg.cc/zb8x8Qyc)

# Лабораторная работа 7

## 1. Тесты для src/lib/text.py (test_text.py)

``` python 
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import pytest
from src.lib.text import normalize, tokenize, count_freq, top_n


@pytest.mark.parametrize(
    "source, expected",
    [
        ("ПрИвЕт\nМИр\t", "привет мир"),
        ("ёжик, Ёлка", "ежик, елка"),
        ("Hello\r\nWorld", "hello world"),
        ("  двойные   пробелы  ", "двойные пробелы"),
        ("", ""),
        ("\n\t\r", ""),
        ("    a    b    ", "a b"),
    ],
)
def test_normalize_basic(source, expected):
    assert normalize(source) == expected


@pytest.mark.parametrize(
    "source, expected",
    [
        ("привет мир", ["привет", "мир"]),
        ("hello,world!!!", ["hello", "world"]),
        ("по-настоящему круто", ["по-настоящему", "круто"]),
        ("2025 год", ["2025", "год"]),
        ("emoji 😀 не слово", ["emoji", "не", "слово"]),
        ("", []),
        ("\n\t\r", []),
    ],
)
def test_tokenize_basic(source, expected):
    assert tokenize(source) == expected


def test_count_freq_and_top_n():
    freq = count_freq(["a", "b", "a", "c", "b", "a"])
    assert freq == {"a": 3, "b": 2, "c": 1}
    assert top_n(freq, 2) == [("a", 3), ("b", 2)]
    freq = count_freq([])
    assert freq == {}
    freq = count_freq(["один"])
    assert freq == {"один": 1}


def test_top_n_tie_breaker():
    freq = count_freq(["bb", "aa", "bb", "aa", "cc"])
    assert top_n(freq, 2) == [("aa", 2), ("bb", 2)]
    freq = count_freq(["z", "y", "x"])
    assert top_n(freq, 2) == [("x", 1), ("y", 1)]
    freq = count_freq(["a", "b"])
    assert top_n(freq, 5) == [("a", 1), ("b", 1)]
```

Этот код автоматически тестирует функции нормализации, токенизации, подсчета частот и выборки топ-N слов из текста.

[![001.png](https://i.postimg.cc/G2FnY8kX/001.png)](https://postimg.cc/tZ4cGgv6)

## 2. Тесты для src/lab05/json_csv.py (test_json_csv.py)

``` python
import csv
import json
from pathlib import Path

import pytest

from src.lab05.json_csv import csv_to_json, json_to_csv


def write_json(path: Path, obj):
    # Записывает объект Python в JSON файл с правильным форматированием и кодировкой
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8")


def read_csv_rows(path: Path):
    # Читает CSV файл и возвращает список словарей (каждая строка = словарь)
    with path.open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


def test_json_to_csv_basic(tmp_path: Path):
    # Позитивный сценарий: обычная конвертация JSON в CSV
    src = tmp_path / "people.json"
    dst = tmp_path / "people.csv"
    data = [{"name": "Alice", "age": 22}, {"name": "Bob", "age": 25}]
    write_json(src, data)
    json_to_csv(str(src), str(dst))
    rows = read_csv_rows(dst)
    assert len(rows) == 2
    assert set(rows[0]) >= {"name", "age"}


def test_json_to_csv_missing_fields(tmp_path: Path):
    # Позитивный сценарий: JSON с пропущенными полями
    src = tmp_path / "incomplete.json"
    dst = tmp_path / "incomplete.csv"
    data = [{"name": "Alice", "age": 22}, {"name": "Bob"}]
    write_json(src, data)
    json_to_csv(str(src), str(dst))
    rows = read_csv_rows(dst)
    assert len(rows) == 2
    assert "age" in rows[1]


def test_csv_to_json_basic(tmp_path: Path):
    # Позитивный сценарий: обычная конвертация CSV в JSON
    src = tmp_path / "people.csv"
    dst = tmp_path / "people.json"
    src.write_text("name,age\nAlice,22\nBob,25\n", encoding="utf-8")
    csv_to_json(str(src), str(dst))
    obj = json.loads(dst.read_text(encoding="utf-8"))
    assert isinstance(obj, list) and len(obj) == 2
    assert set(obj[0]) == {"name", "age"}
    assert obj[0]["name"] == "Alice"


def test_csv_to_json_cyrillic(tmp_path: Path):
    # Позитивный сценарий: CSV с кириллицей
    src = tmp_path / "russian.csv"
    dst = tmp_path / "russian.json"
    src.write_text("имя,возраст\nАлиса,22\n", encoding="utf-8")
    csv_to_json(str(src), str(dst))
    obj = json.loads(dst.read_text(encoding="utf-8"))
    assert obj[0]["имя"] == "Алиса"


def test_json_to_csv_empty_raises(tmp_path: Path):
    # Негативный сценарий: пустой JSON файл
    src = tmp_path / "empty.json"
    src.write_text("[]", encoding="utf-8")
    with pytest.raises(ValueError):
        json_to_csv(str(src), str(tmp_path / "out.csv"))


def test_json_to_csv_invalid_raises(tmp_path: Path):
    # Негативный сценарий: некорректный JSON
    src = tmp_path / "invalid.json"
    src.write_text("{bad}", encoding="utf-8")
    with pytest.raises(ValueError):
        json_to_csv(str(src), str(tmp_path / "out.csv"))


def test_csv_to_json_empty_raises(tmp_path: Path):
    # Негативный сценарий: пустой CSV файл
    src = tmp_path / "empty.csv"
    src.write_text("", encoding="utf-8")
    with pytest.raises(ValueError):
        csv_to_json(str(src), str(tmp_path / "out.json"))


def test_csv_to_json_no_data_raises(tmp_path: Path):
    # Негативный сценарий: CSV только с заголовками
    src = tmp_path / "no_data.csv"
    src.write_text("name,age\n", encoding="utf-8")
    with pytest.raises(ValueError):
        csv_to_json(str(src), str(tmp_path / "out.json"))


def test_json_to_csv_missing_file_raises():
    # Негативный сценарий: несуществующий JSON файл
    with pytest.raises(FileNotFoundError):
        json_to_csv("nope.json", "out.csv")


def test_csv_to_json_missing_file_raises():
    # Негативный сценарий: несуществующий CSV файл
    with pytest.raises(FileNotFoundError):
        csv_to_json("nope.csv", "out.json")
```

Этот код автоматически тестирует функции взаимной конвертации между JSON и CSV форматами с проверкой различных сценариев.

[![002.png](https://i.postimg.cc/HxpBZrGY/002.png)](https://postimg.cc/d7x2Dttp)

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

# Лабораторная работа 9

## Group.py

``` python 
import csv
from pathlib import Path
from src.lab08.models import Student

from typing import List

class Group:
    # Класс для управления студентами в CSV-файле. Реализует CRUD-операции: Create, Read, Update, Delete
    
    def __init__(self, storage_path: str):
        # Инициализация группы студентов

        self.path = Path(storage_path)
        if not self.path.exists():
            self.path.write_text("fio,birthdate,group,gpa\n", encoding="utf-8")  # Записать заголовок 

    def _read_all(self):
        # Читаем все записи из CSV-файла и возвращает список словарей

        students = []
        try:
            with open(self.path, 'r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    students.append(row)
        except FileNotFoundError:
            # Если файл не найден, возвращаем пустой список
            pass
        return students

    def _write_all(self, students: List[dict]):
        # Записываем всех студентов в CSV-файл

        with open(self.path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['fio', 'birthdate', 'group', 'gpa'])
            writer.writeheader()
            writer.writerows(students)

    def list(self):
        # Получаем всех студентов
        
        students_data = self._read_all()
        students = []
        for data in students_data:
            # Преобразуем GPA в число с плавающей точкой
            gpa = float(data['gpa'])
            student = Student(
                fio=data['fio'],
                birthdate=data['birthdate'],
                group=data['group'],
                gpa=gpa
            )
            students.append(student)
        return students

    def add(self, student: Student):
        # Добавляем нового студента

        # Читаем существующих студентов
        students = self._read_all()
        
        # Добавляем нового студента
        new_student = {
            'fio': student.fio,
            'birthdate': student.birthdate,
            'group': student.group,
            'gpa': str(student.gpa)  # Преобразуем в строку для CSV
        }
        
        students.append(new_student)
        
        # Записываем обратно в файл
        self._write_all(students)
        print(f"Студент '{student.fio}' успешно добавлен!")
        return True 
         

    def find(self, substr: str):
        # Найти студентов по подстроке в ФИО

        all_students = self.list()
        found_students = []
        
        for student in all_students:
            if substr.lower() in student.fio.lower():
                found_students.append(student)
        
        return found_students

    def remove(self, fio: str):
        # Удалить студента по ФИО
        
        students = self._read_all()
        initial_count = len(students)
        
        # Фильтруем студентов, оставляя только тех, у кого не совпадает ФИО
        students = [s for s in students if s['fio'] != fio]
        
        if len(students) < initial_count:
            self._write_all(students)
            print(f"Студент '{fio}' успешно удален!")
            return True
        else:
            print(f"Студент с ФИО '{fio}' не найден!")
            return False
        
        
    def update(self, fio: str, **fields):
        # Обновить данные студента

        students = self._read_all()
        updated = False
        
        for student in students:
            if student['fio'] == fio:
                # Обновляем указанные поля
                for field, value in fields.items():
                    if field in student:
                        student[field] = str(value)
                        updated = True
                
                if updated:
                    self._write_all(students)
                    print(f"Данные студента '{fio}' успешно обновлены!")
                    return True
        
        print(f"Студент с ФИО '{fio}' не найден!")
        return False
```

Этот код позволяет управлять списком студентов через CSV-файл - добавлять новых, удалять, искать и обновлять их данные, как в простой базе данных.

## Тест (test_lab09.py)

``` python
from src.lab09.group import Group, Student

def main():
    # Создаем группу студентов
    group = Group("data/lab09/students.csv")
    
    print("Изначальный список:\n")
    for s in group.list():
        print(s)
    
    # 1. Добавление студентов (CREATE)
    print("\n1. ДОБАВЛЕНИЕ СТУДЕНТОВ (CREATE):")
    print("-" * 30)
    
    new_student = Student("Горьковой Владислав", "2006-07-23", "БИВТ-25-1", 4.2) # Создаем нового студента
    group.add(new_student) # Добавляем студентов в группу
    
    # 2. Просмотр всех студентов (READ)
    print("\n2. ВСЕ СТУДЕНТЫ (READ):")
    print("-" * 30)
    all_students = group.list()
    for i, student in enumerate(all_students, 1):
        print(f"{i}. {student}")
    
    # 3. Поиск студентов (READ - поиск)
    print("\n3. ПОИСК СТУДЕНТОВ ПО 'Котилевич' (READ - поиск):")
    print("-" * 30)
    found_students = group.find("Котилевич")
    for i, student in enumerate(found_students, 1):
        print(f"{i}. {student}")
    
    # 4. Обновление студента (UPDATE)
    print("\n4. ОБНОВЛЕНИЕ ДАННЫХ СТУДЕНТА (UPDATE):")
    print("-" * 30)
    # Улучшим успеваемость Егора
    group.update("Котилевич Егор Александрович", gpa = 2.4, group = "БИВТ-25-1")
    
    # Проверим, что обновилось
    print("\nПосле обновления:")
    all_students = group.list()
    for i, student in enumerate(all_students, 1):
        print(f"{i}. {student}")
    
    # 5. Удаление студента (DELETE)
    print("\n5. УДАЛЕНИЕ СТУДЕНТА ВЛАДИКА(DELETE):")
    print("-" * 30)
    group.remove("Горьковой Владислав")
    
    # Проверим, что удалилось
    print("\nПосле удаления:")
    all_students = group.list()
    for i, student in enumerate(all_students, 1):
        print(f"{i}. {student}")
    
    
    print("\n" + "=" * 25)
    print("ТЕСТИРОВАНИЕ ЗАВЕРШЕНО!")
    print("=" * 25)
    
    # Показать содержимое CSV файла
    print("\nСОДЕРЖИМОЕ CSV ФАЙЛА:")
    print("-" * 30)
    with open("data/lab09/students.csv", "r", encoding="utf-8") as f:
        print(f.read())

if __name__ == "__main__":
    main()
```

[![8768686784.png](https://i.postimg.cc/4yQTPCnJ/8768686784.png)](https://postimg.cc/m1kqZ5Qq)

[![7887867868.png](https://i.postimg.cc/DyhvX6mV/7887867868.png)](https://postimg.cc/23HNp44T)
[![867868686.png](https://i.postimg.cc/nc1HYmQg/867868686.png)](https://postimg.cc/LnnKmnD3)

# Лабораторная работа 10

## Теоретическая часть

### Стек (Stack)
- **Что это**: Структура данных LIFO (Last In, First Out) - "последним пришел, первым ушел"
- **Аналогия**: Стопка тарелок - новую кладем сверху, и сверху же берем
- **Основные операции**:
  - `push(item)` - добавить на вершину (O(1))
  - `pop()` - снять с вершины (O(1))
  - `peek()` - посмотреть вершину без удаления (O(1))

### Очередь (Queue)
- **Что это**: Структура данных FIFO (First In, First Out) - "первым пришел, первым ушел"
- **Аналогия**: Очередь в магазине - кто первый встал, того первым обслужили
- **Основные операции**:
  - `enqueue(item)` - добавить в конец (O(1))
  - `dequeue()` - взять из начала (O(1))
  - `peek()` - посмотреть первый элемент (O(1))

### Связный список (Singly Linked List)
- **Что это**: Цепочка узлов, где каждый узел содержит значение и ссылку на следующий узел
- **Структура**: `[значение|ссылка] -> [значение|ссылка] -> [значение|None]`
- **Основные операции**:
  - `append(value)` - добавить в конец (O(1) с tail, O(n) без tail)
  - `prepend(value)` - добавить в начало (O(1))
  - `insert(idx, value)` - вставить по индексу (O(n))
  - `remove_at(idx)` - удалить по индексу (O(n))

# Практика

## Structures.py
```python
from collections import deque
from typing import Any

class Stack:
    # Стек (Stack) - структура данных "LIFO" (Last In, First Out)

    
    def __init__(self):
        # Внутреннее хранилище стека
        self._data = []

    def push(self, item):
        # Добавить элемент на вершину стека (в конец) O(1)
        self._data.append(item) # Просто добавляем в конец списка

    def pop(self):
        if self.is_empty():
            raise IndexError("Невозможна операция pop(): стек пуст!")
        return self._data.pop() # pop() без аргументов удаляет последний элемент

    def peek(self):
        # Вернуть верхний элемент без удаления. O(1)
        if self.is_empty():
            return None
        return self._data[-1]

    def is_empty(self) -> bool:
        # Проверить, пуст ли стек. O(1)
        return len(self._data) == 0
    
    def __len__(self) -> int:
        # Количество элементов в стеке. O(1)
        return len(self._data) # Возвращает количество элементов в стеке
    
    def __str__(self) -> str:
        return f"Stack({self._data})" # Строковое представление стека для печати


class Queue:
    # Очередь (Queue) - структура данных "FIFO" (First In, First Out)

    def __init__(self):
        self._data = deque()

    def enqueue(self, item):
        self._data.append(item)  # Добавляем в конец

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Нельзя удалить из пустой очереди!")
        return self._data.popleft()  # Удаляем с начала очереди

    def peek(self):
        if self.is_empty():
            return None
        return self._data[0]  # Вернуть первый элемент без удаления

    def is_empty(self) -> bool:
        return len(self._data) == 0 # Проверить, пуста ли очередь
    
    def __len__(self) -> int:
        return len(self._data) # Возвращает количество элементов в очереди
    
    def __str__(self) -> str:
        return f"Queue({list(self._data)})" # Строковое представление очереди для печати
```

Этот код создаёт две основные структуры данных - стек (где элементы работают по принципу "последний зашёл, первый вышел") и очередь (где "первый зашёл, первый вышел") - с базовыми операциями добавления, удаления и проверки элементов.

## Тест

``` python
from src.lab10.structures import Stack, Queue
from src.lab10.linked_list import SinglyLinkedList

# Тест Stack
print("=== Тест Stack ===")
s = Stack()

# Проверяем пустой стек
print("1. Пустой стек:")
print(f"   is_empty = {s.is_empty()}")  # True
print(f"   peek = {s.peek()}")          # None

# Добавляем элементы
print("\n2. Добавляем 1, 2, 3:")
s.push(1)
s.push(2)
s.push(3)
print(f"   Стек: {s}")
print(f"   Длина: {len(s)}")            # 3
print(f"   peek = {s.peek()}")          # 3

# Удаляем элементы
print("\n3. Удаляем элементы:")
print(f"   pop = {s.pop()}")            # 3
print(f"   pop = {s.pop()}")            # 2
print(f"   Осталось: {s}")

# Проверяем ошибку
print("\n4. Проверка ошибки:")
s.pop()  # удаляем последний
try:
    s.pop()
except IndexError as e:
    print(f"   Ошибка при pop из пустого стека: {e}")

# Тест Queue
print("\n=== Тест Queue ===")
q = Queue()

# Проверяем пустую очередь
print("1. Пустая очередь:")
print(f"   is_empty = {q.is_empty()}")  # True
print(f"   peek = {q.peek()}")          # None

# Добавляем элементы
print("\n2. Добавляем 'a', 'b', 'c':")
q.enqueue('a')
q.enqueue('b')
q.enqueue('c')
print(f"   Очередь: {q}")
print(f"   Длина: {len(q)}")            # 3
print(f"   peek = {q.peek()}")          # 'a'

# Удаляем элементы
print("\n3. Удаляем элементы:")
print(f"   dequeue = {q.dequeue()}")    # 'a'
print(f"   dequeue = {q.dequeue()}")    # 'b'
print(f"   Осталось: {q}")

# Еще раз проверяем peek и is_empty
print("\n4. Проверяем состояние:")
q.enqueue('d')
print(f"   Добавили 'd': {q}")
print(f"   peek = {q.peek()}")          # 'c'
print(f"   is_empty = {q.is_empty()}")  # False

# Проверяем ошибку
print("\n5. Проверка ошибки:")
q.dequeue()  # 'c'
q.dequeue()  # 'd'
try:
    q.dequeue()
except IndexError as e:
    print(f"   Ошибка при dequeue из пустой очереди: {e}")
```

[![34564645.png](https://i.postimg.cc/x1rZsfWQ/34564645.png)](https://postimg.cc/563pyV4K)


## Linked_list.py
```python
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None  # Хвост - для оптимизации добавления в конец
        self._size = 0  # Начинаем с 0 элементов

    def append(self, value):
        """Добавить элемент в конец списка"""
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:  # Если в списке уже есть элементы
            self.tail.next = new_node  # Старый хвост теперь указывает на новый узел
            self.tail = new_node  # Новый узел становится хвостом
        
        self._size += 1  # Не забываем увеличить счетчик!
        

    def prepend(self, value):
        new_node = Node(value)
        
        if self.head is None:  # Если список пустой
            self.head = new_node
            self.tail = new_node
        else:  # Если в списке уже есть элементы
            new_node.next = self.head  # Новый узел указывает на старую голову
            self.head = new_node  # Новый узел становится головой
        
        self._size += 1

    def insert(self, idx, value):
        """Вставка по индексу O(n)"""
        # Проверяем, что индекс в допустимых пределах
        if idx < 0 or idx > self._size:
            raise IndexError(f"Index {idx} out of range [0, {self._size}]")
        
        # Если вставляем в начало
        if idx == 0:
            self.prepend(value)
            return
        
        if idx == self._size:
            self.append(value)
            return
        
        # Ищем позицию для вставки
        current = self.head
        # Переходим к узлу перед нужной позицией
        for _ in range(idx - 1):
            current = current.next
        
        # Вставляем новый узел
        new_node = Node(value, next=current.next)
        current.next = new_node
        
        # ИСПРАВЛЕНО: увеличиваем размер
        self._size += 1

    def __iter__(self):
        """Итератор по значениям списка"""
        current = self.head
        while current is not None:
            yield current.value
            current = current.next

    def __len__(self):
        """Возвращает количество элементов O(1)"""
        return self._size

    def __repr__(self):
        """Строковое представление списка"""
        values = list(self)
        return f"SinglyLinkedList({values})"
```

Этот код создаёт односвязный список, в котором можно добавлять элементы в начало, конец или в любое место по индексу, поддерживая их последовательную связь через узлы.

## Тест

``` python
print("=== Тест SinglyLinkedList ===")
lst = SinglyLinkedList()

# Проверяем пустой список
print("1. Пустой список:")
print(f"   Список: {lst}")
print(f"   Длина: {len(lst)}")          # 0

# Добавляем в конец
print("\n2. Добавляем в конец (append):")
lst.append(10)
lst.append(20)
lst.append(30)
print(f"   После append: {lst}")
print(f"   Длина: {len(lst)}")          # 3

# Добавляем в начало
print("\n3. Добавляем в начало (prepend):")
lst.prepend(5)
print(f"   После prepend(5): {lst}")

# Вставляем по индексу
print("\n4. Вставляем по индексу (insert):")
lst.insert(2, 15)
print(f"   После insert(2, 15): {lst}")

# Проверяем итерацию
print("\n5. Проверяем цикл for:")
print("   Элементы:", end=" ")
for x in lst:
    print(x, end=" ")
print()

# Проверяем граничные случаи
print("\n6. Граничные случаи:")
lst.insert(0, 1)      # в начало
lst.insert(len(lst), 100)  # в конец
print(f"   После insert в начало и конец: {lst}")

# Проверяем ошибки
print("\n7. Проверяем ошибки:")
try:
    lst.insert(-5, 999)
except IndexError as e:
    print(f"   Ошибка при insert(-5): {e}")

try:
    lst.insert(100, 100)
except IndexError as e:
    print(f"   Ошибка при insert(100): {e}")
```

[![546456464.png](https://i.postimg.cc/hGc5BCD3/546456464.png)](https://postimg.cc/RWpR1Lnc)
