import sys
import os
from pathlib import Path

# Добавляем корневую директорию проекта в Python path
current_dir = Path(__file__).parent
project_root = current_dir.parent.parent  # Поднимаемся на 2 уровня вверх от src/lab05
sys.path.insert(0, str(project_root))

from src.lab05.json_csv import json_to_csv, csv_to_json
from src.lab05.csv_xlsx import csv_to_xlsx

def main():
    """Тестирование всех функций конвертации"""
    
    print("=== Лабораторная работа №5 - Тестирование конвертаций ===")
    
    try:
        # 1. JSON → CSV
        print("\n1. Конвертация JSON → CSV")
        json_to_csv('data/samples/people.json', 'data/out/people_from_json.csv')
        print("✓ people.json → people_from_json.csv")
        
        # 2. CSV → JSON
        print("\n2. Конвертация CSV → JSON")
        csv_to_json('data/samples/people.csv', 'data/out/people_from_csv.json')
        print("✓ people.csv → people_from_csv.json")
        
        # 3. CSV → XLSX
        print("\n3. Конвертация CSV → XLSX")
        csv_to_xlsx('data/samples/people.csv', 'data/out/people.xlsx')
        print("✓ people.csv → people.xlsx")
        
        csv_to_xlsx('data/samples/cities.csv', 'data/out/cities.xlsx')
        print("✓ cities.csv → cities.xlsx")
        
        print("\n=== Все конвертации выполнены успешно! ===")
        print("\nСозданные файлы:")
        print("- data/out/people_from_json.csv")
        print("- data/out/people_from_csv.json") 
        print("- data/out/people.xlsx")
        print("- data/out/cities.xlsx")
        
    except Exception as e:
        print(f"\n✗ Ошибка: {e}")

if __name__ == "__main__":
    main()