import argparse
from pathlib import Path
from src.lib.text import tokenize, count_freq, top_n

def main():
    """
        1. cat   — вывод содержимого текстового файла (с нумерацией строк при флаге -n);
        2. stats — анализ частот встречаемости слов в тексте. (с указанием количества слов в топе --top n, иначе автоматически top 5)
    """

    parser = argparse.ArgumentParser(description="CLI‑утилиты лабораторной №6") #создание парсера с описанием команд
    subparsers = parser.add_subparsers(dest="command") #dest="command" - значение выбранной команды будет храниться в args.command

    # подкоманда cat
    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True) #required=True - обязательный элемент, хранит в себе путь к файлу
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки") #action="store_true" - флаг, который становится True если указан, иначе False

    # подкоманда stats
    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", required=True)
    stats_parser.add_argument("--top", type=int, default=5) #дополнительный элемент, если его нет - автоматически 5

    args = parser.parse_args() #расшифровывает введенную строку по флагам, указанным ранее

    file=Path(args.input)

    if not file.exists():
        raise FileNotFoundError("Файл не найден")


    if args.command == "cat":
        #python -m src.lab06.cli_text cat --input data/samples/test.txt -n

        with open(file, "r", encoding="utf-8") as f:
            num = 1
            for line in f:
                line = line.rstrip("\n")
                if args.n:
                    print(f"{num}: {line}")
                    num += 1
                else:
                    print(line)

    elif args.command == "stats":
        #python -m src.lab06.cli_text stats --input data/samples/test.txt --top 3

        with open(file, "r", encoding="utf-8") as f:
            data = [row for row in f]
        data = "".join(data)
    
        tokens = tokenize(data)
        freq = count_freq(tokens)
        top = top_n(freq, args.top)
    
        print(f"Топ-{args.top} слов в файле '{args.input}':")
        number = 1
        for word, count in top:
            print(f"{number}. '{word}' - {count} раз")
            number += 1

if __name__ == "__main__":
    main()