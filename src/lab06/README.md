# Лабораторная работа 6

## Подкоманды в одном CLI

``` python 
import argparse

def main():
    parser = argparse.ArgumentParser(description="CLI‑утилиты лабораторной №6")
    subparsers = parser.add_subparsers(dest="command")

    # подкоманда cat
    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True)
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    # подкоманда stats
    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", required=True)
    stats_parser.add_argument("--top", type=int, default=5)

    args = parser.parse_args()

    if args.command == "cat":
        """ Реализация команды cat """
    elif args.command == "stats":
        """ Реализация команды stats """
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
