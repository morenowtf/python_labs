## Лабораторная работа 5

### Задание А

``` python 
from pathlib import Path
import json,csv,sys
sys.path.append('C:/Users/dasha/Desktop/python_labs/src')
from lab04.io_txt_csv import ensure_parent_dir

def json_to_csv(json_path: str, csv_path: str) -> None:
    '''Функция конвертирует JSON-файл в CSV-файл, проверяя синтаксис и корректность входного и создавая директорию(если надо) выходного'''
    j_path=Path(json_path)

    if not j_path.exists(): #проверяем наличие файла
        raise FileNotFoundError('Файл не найден')
    
    with open(j_path,'r',encoding='utf-8') as j_file: #открываем JSON-файл для чтения

        try:
            j_data=json.load(j_file) #загружаем данные из JSON-файла
        except json.JSONDecodeError: #проверяем синтаксис 
            raise ValueError("Пустой JSON или неподдерживаемая структура")
        
        if not j_data: #проверяем файл на пустоту
            raise ValueError('Файл JSON пуст')
        
        if not isinstance(j_data,list): #проверям тип данных(список)
            raise ValueError('Файл не является СПИСКОМ словарей')
        
        if not all(isinstance(row,dict) for row in j_data): #проверяем тип данных(словари)
            raise ValueError('Файл не является списком СЛОВАРЕЙ')
        
    c_path=Path(csv_path)
    ensure_parent_dir(c_path) #создаем родительскую директорию, если ее нет

    with open(c_path,'w',encoding='utf-8', newline='') as c_file: #открываем CSV-файл для записи
        c_writer=csv.DictWriter(c_file,fieldnames=j_data[0].keys()) #команда-помощник для записи CSV, заголовки-ключи первого словаря
        c_writer.writeheader() #записываем заголовки
        c_writer.writerows(j_data) #записываем данные




def csv_to_json(csv_path: str, json_path: str) -> None:
    '''Функция конвертирует CSV-файл в JSON-файл, проверяя синтаксис и корректность входного и создавая директорию(если надо) выходного'''
    c_path=Path(csv_path)

    if not c_path.exists(): #проверяем наличие файла
        raise FileNotFoundError('Файл не найден')
    if c_path.suffix != '.csv': #проверяем расширение файла
            raise ValueError("Неверный тип файла")
    
    with open(c_path,'r',encoding='utf-8') as c_file: #открываем CSV-файл для чтения
        c_data=csv.DictReader(c_file) #команда-помощник для чтения CSV
        if not c_data.fieldnames: #проверяем наличие заголовков
            raise ValueError('Файл пустой или в нем нет заголовков')
        c_rows=list(c_data)
        if not c_rows: #проверяем наличие данных
            raise ValueError('В файле есть заголовки, но нет данных')
        
    j_path=Path(json_path)
    ensure_parent_dir(j_path) #создаем родительскую директорию, если ее нет
    with open(j_path,'w', encoding='utf-8') as j_file: #открываем JSON-файл для записи
        json.dump(c_rows,j_file,ensure_ascii=False,indent=2) #записываем данные в JSON-файл с форматированием(кириллица и отступы)


```
![Картинка 1](./images/lab05/json_csv.png)
![Картинка 2](./images/lab05/people_json_csv.png)
![Картинка 3](./images/lab05/students_recipes_json_csv.png)

### Задание В

``` python
from openpyxl import Workbook #библиотека и функция для работы с Excel-файлами
from openpyxl.utils import get_column_letter # функция для преобразования номера колонки в букву
import csv,sys
from pathlib import Path
sys.path.append('C:/Users/dasha/Desktop/python_labs/src')
from lab04.io_txt_csv import ensure_parent_dir

def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    '''Функция конвертирует CSV-файл в XSLX-файл, проверяя синтаксис и корректность входного и создавая директорию(если надо) выходного'''
    c_path=Path(csv_path)
    
    if not c_path.exists(): #проверяем наличие файла
        raise FileNotFoundError('Файл не найден')
    if c_path.suffix != '.csv': #проверяем расширение файла
            raise ValueError("Неверный тип файла")
    
    wb = Workbook() #создание новой Excel-книги
    ws = wb.active #получение активного листа
    ws.title = "Sheet1" #установка названия листа

    with open(c_path,'r',encoding='utf-8') as c_file: #открываем CSV-файл для чтения
        c_data=csv.DictReader(c_file) #команда-помощник для чтения CSV
        if not c_data.fieldnames: #проверяем наличие заголовков
            raise ValueError('Файл пустой или в нем нет заголовков')     
        ws.append(c_data.fieldnames) #записываем заголовки в первую строку Excel
        for row in c_data: 
            ws.append([row[field] for field in c_data.fieldnames]) #записываем данные построчно в Excel

    x_path=Path(xlsx_path)
    ensure_parent_dir(x_path) #создаем родительскую директорию, если ее нет
    for column in ws.columns: #проходимся по каждой колонке листа
            max_length=8 #задаем значение минимальной ширины
            column_letter = get_column_letter(column[0].column) #получаем буквенное значение текущей колонки
            for cell in column: #проходимя по каждой ячейке колонки
                max_length = max(len(str(cell.value)), max_length) #обновляем максимальную длину(или нет)
            ws.column_dimensions[column_letter].width = max_length #устанавливаем максимальную ширину для данной колонки
    wb.save(x_path) #сохраяем Excel-файл

```

![Картинка 4](./images/lab05/csv_xslx.png)
![Картинка 5](./images/lab05/cities_csv_xslx.png)
![Картинка 6](./images/lab05/weather_csv_xslx.png)
