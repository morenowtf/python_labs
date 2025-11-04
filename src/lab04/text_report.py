#!/usr/bin/env python3
import sys
import argparse
from pathlib import Path
from typing import List, Tuple, Dict

# Добавляем путь к модулям
sys.path.append(str(Path(__file__).parent.parent))

from lib.text import normalize, tokenize, count_freq, top_n
from lab04.io_txt_csv import read_text, write_csv, ensure_parent_dir


def process_single_file(input_file: str, output_file: str, encoding: str = "utf-8") -> None:
    """
    Обрабатывает один файл: читает, анализирует текст и создает CSV отчет.
    
    Args:
        input_file: Путь к входному файлу
        output_file: Путь для сохранения CSV отчета
        encoding: Кодировка входного файла
    """
    try:
        # Чтение файла
        text = read_text(input_file, encoding)
        
        # Обработка текста
        normalized_text = normalize(text)
        tokens = tokenize(normalized_text)
        freq = count_freq(tokens)
        sorted_words = top_n(freq, len(freq))  # Получаем все слова отсортированными
        
        # Подготовка данных для CSV
        csv_rows = [(word, count) for word, count in sorted_words]
        
        # Создание директорий если нужно
        ensure_parent_dir(output_file)
        
        # Запись CSV
        write_csv(csv_rows, output_file, header=("word", "count"))
        
        # Вывод статистики в консоль
        total_words = len(tokens)
        unique_words = len(freq)
        top_5 = top_n(freq, 5)
        
        print(f"Всего слов: {total_words}")
        print(f"Уникальных слов: {unique_words}")
        print("Топ-5:")
        for word, count in top_5:
            print(f"{word}: {count}")
            
    except FileNotFoundError:
        print(f"Ошибка: Файл '{input_file}' не найден")
        sys.exit(1)
    except UnicodeDecodeError as e:
        print(f"Ошибка кодировки: {e}")
        print("Попробуйте указать другую кодировку через --encoding")
        sys.exit(1)
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description='Анализ текста и генерация CSV отчета')
    parser.add_argument('--in', dest='input_file', default='data/lab04/input.txt',
                       help='Входной текстовый файл (по умолчанию: data/lab04/input.txt)')
    parser.add_argument('--out', dest='output_file', default='data/lab04/report.csv',
                       help='Выходной CSV файл (по умолчанию: data/lab04/report.csv)')
    parser.add_argument('--encoding', dest='encoding', default='utf-8',
                       help='Кодировка входного файла (по умолчанию: utf-8)')
    
    args = parser.parse_args()
    
    print(f"Обработка файла: {args.input_file}")
    print(f"Кодировка: {args.encoding}")
    print(f"Выходной файл: {args.output_file}")
    print("-" * 40)
    
    process_single_file(args.input_file, args.output_file, args.encoding)


if __name__ == "__main__":
    main()