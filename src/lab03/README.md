# Лабораторная работа 3
## Задание A (text.py)
```python
import re

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    #Функция приводит текст к единому регистру и стилю
    s=text
    if casefold :
        s=s.casefold()
    if yo2e :
        s=s.replace("ё","е").replace("Ё","Е")
    s=s.replace("\t"," ").replace("\r"," ").replace("\n"," ")
    s = ' '.join(s.split())
    s=s.strip()

    return s

def tokenize(text: str) -> list[str]:
    #Функция разбивает текст на «слова» по небуквенно-цифровым разделителям
    pattern= r'\w+(?:-\w+)*'
    tokenstext = re.findall(pattern, text)

    return tokenstext

def count_freq(tokens: list[str]) -> dict[str, int]:
    #Функция возвращает словарь слово - количество
    counts={}
    for word in tokens:
        counts[word]=counts.get(word,0)+1
    return counts

def sort_key(item):
    return [-item[1], item[0]]

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    #Функция возвращает топ-N по убыванию частоты
    sorted_freq= sorted(freq.items(),key=sort_key)
    top_n=[]

    for i in range(min(n, len(sorted_freq))):
        top_n.append((sorted_freq[i][0], sorted_freq[i][1]))

    return top_n

def summary(text):
    normalized_text = normalize(text)

    tokens = tokenize(normalized_text)

    total_words = len(tokens)
    freq_sorted = count_freq(tokens)
    unique_words = len(freq_sorted)
    top = top_n(freq_sorted, 5)

    print(f"Всего слов: {total_words}")
    print(f"Уникальных слов: {unique_words}")
    print("Топ-5:")

    for word, count in top:
        print(f"{word}:{count}")
```
Скрипт анализирует текст, подсчитывая слова и выводя статистику по частотности.

Для теста этого скрипта, я написал второй скрипт, в котором происходит вызов этих методов (test_case.py)
```python
import sys
import os

# Добавляем корневую директорию проекта в путь поиска модулей
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, project_root)

from src.lib.text import *

print(normalize("ПрИвЕт\nМИр\t"))
print(normalize("ёжик, Ёлка", yo2e=True))
print(normalize("Hello\r\nWorld"))
print(normalize("  двойные   пробелы  "))


print(tokenize("привет мир"))
print(tokenize("hello,world!!!"))
print(tokenize("по-настоящему круто"))
print(tokenize("2025 год"))
print(tokenize("emoji 😀 не слово"))

print(top_n(count_freq(["a", "b", "a", "c", "b", "a"]), n=2))
print(top_n(count_freq(["bb", "aa", "bb", "aa", "cc"]), n=2))
```
При запуске этого скрипта, получаем вот такой результат:

[![401.png](https://i.postimg.cc/ZnJCPzsD/401.png)](https://postimg.cc/S2tSq3hW)

## Задание B (text_stats.py)

```python
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from src.lib.text import normalize, tokenize, count_freq, top_n

def main():
    # Читаем весь вход до EOF
    input_text = sys.stdin.readline()


    # Нормализация
    text_norm = normalize(input_text)
    # Токенизация
    tokens = tokenize(text_norm)
    # Подсчёт частот
    freq = count_freq(tokens)

    # Подсчёт статистики
    words_total = len(tokens)
    unique_words = len(freq)

    # Топ 5 слов
    top_words = top_n(freq, 5)

    print(f"Всего слов: {words_total}")
    print(f"Уникальных слов: {unique_words}")
    print("Топ-5:")
    for word, count in top_words:
        print(f"{word}:{count}")

if __name__ == "__main__":
    main()
```
Этот скрипт анализирует текст из stdin и выводит статистику по словам.
Запускаем этот скрипт, он ожидает ввод текста от нас, мы вводим "Привет, мир! Привет!!!", и получаем вот такой результат:

[![402.png](https://i.postimg.cc/x878wN1T/402.png)](https://postimg.cc/kRQ784Sk)

