import re
from collections import Counter

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if casefold:
        text = text.casefold()
    if yo2e:
        text = text.replace('ё', 'е').replace('Ё', 'Е')
    # Заменяем управляющие символы на пробелы:
    text = re.sub(r'[\t\r\n]+', ' ', text)
    # Убираем множественные пробелы и лишние пробелы по краям:
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def tokenize(text: str) -> list[str]:
    # Находим все слова, где допускается дефис внутри
    return re.findall(r'\w+(?:-\w+)*', text)


def count_freq(tokens: list[str]) -> dict[str, int]:
    return dict(Counter(tokens))


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    # Сортировка по (-частота, слово)
    return sorted(freq.items(), key=lambda x: (-x[1], x[0]))[:n]



print(normalize("ПрИвЕт\nМИр\t"))
print(normalize("ёжик, Ёлка"))
print(normalize("Hello\r\nWorld"))
print(normalize("  двойные   пробелы  "))

print(tokenize("привет мир"))
print(tokenize("hello,world!!!"))
print(tokenize("по-настоящему круто"))
print(tokenize("2025 год"))
print(tokenize("emoji 😀 не слово"))

print(count_freq(["a","b","a","c","b","a"]))
print(top_n(["bb","aa","bb","aa","cc"]))