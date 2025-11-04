# read_text / write_csv (+ ensure_parent_dir)
import csv
from pathlib import Path
from typing import Iterable, Sequence
from collections import Counter
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from lib.text import normalize, tokenize, count_freq, top_n


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """Читает текстовый файл и возвращает его содержимое в виде строки.
    
    Аргументы:
    path: Путь к файлу (строка или Path-объект)
    encoding: Кодировка файла
    
    Возвращает:
    Содержимое файла как строку"""
        
    p = Path(path)
    # FileNotFoundError и UnicodeDecodeError пусть «всплывают» — это нормально
    return p.read_text(encoding=encoding)

def write_csv(rows: Iterable[Sequence], path: str | Path,
              header: tuple[str, ...] | None = None) -> None:
    """Записывает данные в CSV-файл, создавая при необходимости родительские директории.
    
    Аргументы:
    rows: Итерируемый объект со строками данных
    path: Путь для сохранения CSV-файла
    header: Опциональный заголовок для CSV
    """
    p = Path(path)
    rows = list(rows)
    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header) # Записываем заголовок если он предоставлен
        for r in rows:
            w.writerow(r) # Записываем каждую строку данных

def frequencies_from_text(text: str) -> dict[str, int]:
    """Вычисляет частоты слов в тексте после нормализации и токенизации.
    Принимает - text: Исходный текст для анализа | Возвращает - Словарь с частотой каждого слова"""

    tokens = tokenize(normalize(text)) # Нормализация -> токенизация
    return Counter(tokens)  # Подсчет частот с помощью Counter

def sorted_word_counts(freq: dict[str, int]) -> list[tuple[str, int]]:
    """Сортирует словарь частот по убыванию частоты и лексикографически.
    Принимает - freq: Словарь с частотами слов | Возвращает - Отсортированный список кортежей (слово, частота)"""
    
    # Сортировка сначала по убыванию частоты (-kv[1]), 
    # затем по алфавиту (kv[0])
    return sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))