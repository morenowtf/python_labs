# Лабораторная работа 6

## Подкоманды в одном CLI

``` python 
import argparse
from pathlib import Path
from src.lib.text import tokenize, count_freq, top_n

def main():
    # Инициализация парсера аргументов командной строки
    parser = argparse.ArgumentParser(description="CLI-утилита для анализа текстовых файлов")
    subparsers = parser.add_subparsers(dest="command", help="Доступные команды")

    # Парсер для команды cat
    cat_parser = subparsers.add_parser("cat", help="Вывод содержимого файла")
    cat_parser.add_argument("--input", required=True, help="Путь к входному файлу")
    cat_parser.add_argument("-n", action="store_true", help="Включить нумерацию строк")

    # Парсер для команды stats
    stats_parser = subparsers.add_parser("stats", help="Статистика частоты слов")
    stats_parser.add_argument("--input", required=True, help="Путь к анализируемому файлу")
    stats_parser.add_argument("--top", type=int, default=5, help="Количество топ-слов (по умолчанию: 5)")

    args = parser.parse_args()
    file_path = Path(args.input)

    # Проверка существования файла
    if not file_path.exists():
        raise FileNotFoundError(f"Файл {args.input} не существует")

    if args.command == "cat":
        # python -m src.lab06.cli_text cat --input data/samples/test.txt -n
        with open(file_path, "r", encoding="utf-8") as file:
            for line_num, line in enumerate(file, 1):
                line = line.rstrip("\n")
                if args.n:
                    print(f"{line_num}: {line}")
                else:
                    print(line)

    elif args.command == "stats":
        # python -m src.lab06.cli_text stats --input data/samples/test.txt --top 3
        with open(file_path, "r", encoding="utf-8") as file:
            text_content = file.read()

        # Анализ текста
        tokens = tokenize(text_content)
        frequencies = count_freq(tokens)
        top_words = top_n(frequencies, args.top)

        # Форматированный вывод результатов
        print(f"Топ-{args.top} слов в файле '{args.input}':")
        for rank, (word, count) in enumerate(top_words, 1):
            print(f"{rank}. '{word}' - {count}")
```

Этот код содержит две функции для конвертации между JSON и CSV форматами: json_to_csv преобразует JSON-файл в CSV, а csv_to_json выполняет обратное преобразование.

[![41.png](https://i.postimg.cc/Rh59fj8G/41.png)](https://postimg.cc/8JHqgnTr)
[![42.png](https://i.postimg.cc/4xNGzv8L/42.png)](https://postimg.cc/jL9BTfYP)

## CLI‑конвертер

``` python
import argparse
from src.lab05.json_csv import json_to_csv, csv_to_json
from src.lab05.csv_xlsx import csv_to_xlsx

def main():
    parser = argparse.ArgumentParser(description="Конвертеры данных")
    sub = parser.add_subparsers(dest="cmd")

    p1 = sub.add_parser("json2csv")
    p1.add_argument("--in", dest="input", required=True)
    p1.add_argument("--out", dest="output", required=True)

    p2 = sub.add_parser("csv2json")
    p2.add_argument("--in", dest="input", required=True)
    p2.add_argument("--out", dest="output", required=True)

    p3 = sub.add_parser("csv2xlsx")
    p3.add_argument("--in", dest="input", required=True)
    p3.add_argument("--out", dest="output", required=True)

    args = parser.parse_args()

    """
        Вызываем код в зависимости от аргументов.
    """
```

Этот код конвертирует CSV-файл в XLSX-формат с автоматической настройкой ширины колонок.
[![43.png](https://i.postimg.cc/FHBRWFBQ/43.png)](https://postimg.cc/87LNsGGy)
[![44.png](https://i.postimg.cc/xCK11vjx/44.png)](https://postimg.cc/9RQhxq7Z)
