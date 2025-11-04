import sys
import os
from pathlib import Path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from lab04.io_txt_csv import read_text, write_csv, sorted_word_counts, frequencies_from_text
from lib.text import summary  # Импорт функции для анализа текста

def main():
    # Читаем текстовый файл, анализируем его содержимое и генерируем CSV-отчет с частотой слов

    try:        
        # Чтение содержимого текстового файла
        content = read_text("./data/lab04/input.txt")
        
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
                header=("word", "freq")
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