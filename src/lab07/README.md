# Лабораторная работа 7

## 1. Тесты для src/lib/text.py (test_text.py)

``` python 
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import pytest
from src.lib.text import normalize, tokenize, count_freq, top_n


@pytest.mark.parametrize(
    "source, expected",
    [
        ("ПрИвЕт\nМИр\t", "привет мир"),
        ("ёжик, Ёлка", "ежик, елка"),
        ("Hello\r\nWorld", "hello world"),
        ("  двойные   пробелы  ", "двойные пробелы"),
        ("", ""),
        ("\n\t\r", ""),
        ("    a    b    ", "a b"),
    ],
)
def test_normalize_basic(source, expected):
    assert normalize(source) == expected


@pytest.mark.parametrize(
    "source, expected",
    [
        ("привет мир", ["привет", "мир"]),
        ("hello,world!!!", ["hello", "world"]),
        ("по-настоящему круто", ["по-настоящему", "круто"]),
        ("2025 год", ["2025", "год"]),
        ("emoji 😀 не слово", ["emoji", "не", "слово"]),
        ("", []),
        ("\n\t\r", []),
    ],
)
def test_tokenize_basic(source, expected):
    assert tokenize(source) == expected


def test_count_freq_and_top_n():
    freq = count_freq(["a", "b", "a", "c", "b", "a"])
    assert freq == {"a": 3, "b": 2, "c": 1}
    assert top_n(freq, 2) == [("a", 3), ("b", 2)]
    freq = count_freq([])
    assert freq == {}
    freq = count_freq(["один"])
    assert freq == {"один": 1}


def test_top_n_tie_breaker():
    freq = count_freq(["bb", "aa", "bb", "aa", "cc"])
    assert top_n(freq, 2) == [("aa", 2), ("bb", 2)]
    freq = count_freq(["z", "y", "x"])
    assert top_n(freq, 2) == [("x", 1), ("y", 1)]
    freq = count_freq(["a", "b"])
    assert top_n(freq, 5) == [("a", 1), ("b", 1)]
```

Этот код автоматически тестирует функции нормализации, токенизации, подсчета частот и выборки топ-N слов из текста.

[![001.png](https://i.postimg.cc/G2FnY8kX/001.png)](https://postimg.cc/tZ4cGgv6)

## 2. Тесты для src/lab05/json_csv.py (test_json_csv.py)

``` python
import csv
import json
from pathlib import Path

import pytest

from src.lab05.json_csv import csv_to_json, json_to_csv


def write_json(path: Path, obj):
    # Записывает объект Python в JSON файл с правильным форматированием и кодировкой
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8")


def read_csv_rows(path: Path):
    # Читает CSV файл и возвращает список словарей (каждая строка = словарь)
    with path.open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


def test_json_to_csv_basic(tmp_path: Path):
    # Позитивный сценарий: обычная конвертация JSON в CSV
    src = tmp_path / "people.json"
    dst = tmp_path / "people.csv"
    data = [{"name": "Alice", "age": 22}, {"name": "Bob", "age": 25}]
    write_json(src, data)
    json_to_csv(str(src), str(dst))
    rows = read_csv_rows(dst)
    assert len(rows) == 2
    assert set(rows[0]) >= {"name", "age"}


def test_json_to_csv_missing_fields(tmp_path: Path):
    # Позитивный сценарий: JSON с пропущенными полями
    src = tmp_path / "incomplete.json"
    dst = tmp_path / "incomplete.csv"
    data = [{"name": "Alice", "age": 22}, {"name": "Bob"}]
    write_json(src, data)
    json_to_csv(str(src), str(dst))
    rows = read_csv_rows(dst)
    assert len(rows) == 2
    assert "age" in rows[1]


def test_csv_to_json_basic(tmp_path: Path):
    # Позитивный сценарий: обычная конвертация CSV в JSON
    src = tmp_path / "people.csv"
    dst = tmp_path / "people.json"
    src.write_text("name,age\nAlice,22\nBob,25\n", encoding="utf-8")
    csv_to_json(str(src), str(dst))
    obj = json.loads(dst.read_text(encoding="utf-8"))
    assert isinstance(obj, list) and len(obj) == 2
    assert set(obj[0]) == {"name", "age"}
    assert obj[0]["name"] == "Alice"


def test_csv_to_json_cyrillic(tmp_path: Path):
    # Позитивный сценарий: CSV с кириллицей
    src = tmp_path / "russian.csv"
    dst = tmp_path / "russian.json"
    src.write_text("имя,возраст\nАлиса,22\n", encoding="utf-8")
    csv_to_json(str(src), str(dst))
    obj = json.loads(dst.read_text(encoding="utf-8"))
    assert obj[0]["имя"] == "Алиса"


def test_json_to_csv_empty_raises(tmp_path: Path):
    # Негативный сценарий: пустой JSON файл
    src = tmp_path / "empty.json"
    src.write_text("[]", encoding="utf-8")
    with pytest.raises(ValueError):
        json_to_csv(str(src), str(tmp_path / "out.csv"))


def test_json_to_csv_invalid_raises(tmp_path: Path):
    # Негативный сценарий: некорректный JSON
    src = tmp_path / "invalid.json"
    src.write_text("{bad}", encoding="utf-8")
    with pytest.raises(ValueError):
        json_to_csv(str(src), str(tmp_path / "out.csv"))


def test_csv_to_json_empty_raises(tmp_path: Path):
    # Негативный сценарий: пустой CSV файл
    src = tmp_path / "empty.csv"
    src.write_text("", encoding="utf-8")
    with pytest.raises(ValueError):
        csv_to_json(str(src), str(tmp_path / "out.json"))


def test_csv_to_json_no_data_raises(tmp_path: Path):
    # Негативный сценарий: CSV только с заголовками
    src = tmp_path / "no_data.csv"
    src.write_text("name,age\n", encoding="utf-8")
    with pytest.raises(ValueError):
        csv_to_json(str(src), str(tmp_path / "out.json"))


def test_json_to_csv_missing_file_raises():
    # Негативный сценарий: несуществующий JSON файл
    with pytest.raises(FileNotFoundError):
        json_to_csv("nope.json", "out.csv")


def test_csv_to_json_missing_file_raises():
    # Негативный сценарий: несуществующий CSV файл
    with pytest.raises(FileNotFoundError):
        csv_to_json("nope.csv", "out.json")
```

Этот код автоматически тестирует функции взаимной конвертации между JSON и CSV форматами с проверкой различных сценариев.

[![002.png](https://i.postimg.cc/HxpBZrGY/002.png)](https://postimg.cc/d7x2Dttp)
