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

# Точка входа в программу
if __name__ == "__main__":
    main()