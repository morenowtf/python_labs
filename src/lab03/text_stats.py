import sys
from lib.text import count_words, count_unique, top_n

def main():
    text = sys.stdin.read()
    words_count = count_words(text)
    unique_count = count_unique(text)
    top5 = top_n(text, 5)

    print(f"Всего слов: {words_count}")
    print(f"Уникальных слов: {unique_count}")
    print("Топ-5:")
    for word, freq in top5:
        print(f"{word}:{freq}")

if __name__ == "__main__":
    main()
