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