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