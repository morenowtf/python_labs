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

Этот код содержит две функции для конвертации между JSON и CSV форматами: json_to_csv преобразует JSON-файл в CSV, а csv_to_json выполняет обратное преобразование.

[![41.png](https://i.postimg.cc/Rh59fj8G/41.png)](https://postimg.cc/8JHqgnTr)
[![42.png](https://i.postimg.cc/4xNGzv8L/42.png)](https://postimg.cc/jL9BTfYP)

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

Этот код конвертирует CSV-файл в XLSX-формат с автоматической настройкой ширины колонок.
[![43.png](https://i.postimg.cc/FHBRWFBQ/43.png)](https://postimg.cc/87LNsGGy)
[![44.png](https://i.postimg.cc/xCK11vjx/44.png)](https://postimg.cc/9RQhxq7Z)
