# python_labs
# Лабораторная работа 1
### Задание 1
```python
name = input("Введите ваше имя: ")
age = int(input("Введите ваш возраст: "))

print(f"Привет, {name}! Через год тебе будет {age + 1}.")
```
Считываем дни, считываем возраст, затем вывод эту информацию, предватирительно прибавив один год к возрасту

[![img1.png](https://i.postimg.cc/DmkF39QK/img1.png)](https://postimg.cc/0KfhpHHt)

### Задание 2
```python
firstNumber = input("Введите первое число: ").replace(",", ".")
secondNumber = input("Введите второе число: ").replace(',', '.')

summary = float(firstNumber) + float(secondNumber)
avg = (summary / 2 )

print(f"Сумма = {summary} ; Среднее арифметическое = {avg}")
```
[![img2.png](https://i.postimg.cc/PxT292vF/img2.png)](https://postimg.cc/jW3HJ6Xz)

### Задание 3
```python
price = float(input("Введите цену: "))
discount = float(input("Введите процент скидки: "))
vat = float(input("Введите процент налогов: "))

base = price * (1 - discount / 100)
vat_amount = base * (vat/100)
total = base + vat_amount

print(f"База после скидки: {base:.2f} ₽ \nНДС: {vat_amount:.2f} ₽ \nИтого к оплате: {total:.2f} ₽")
```
[![img3.png](https://i.postimg.cc/yYMh2vwX/img3.png)](https://postimg.cc/LnVZ1B4n)

### Задание 4
```python
minutes = int(input("Введите минуты: "))

hours = minutes // 60
remaining_minutes = minutes % 60

print(f"Минуты: {minutes} \n{hours}:{remaining_minutes:02d}")
```
[![img44.png](https://i.postimg.cc/xC5KjjHy/img44.png)](https://postimg.cc/1nggJQvf)

### Задание 5
```python
fullName = input("Введите ФИО: ")

uppercase = ""
for char in fullName:
    if char.isupper():
        uppercase += char

strLength = len(fullName.replace(" ", ""))

print(f"Инициалы: {uppercase} \nКоличество символов без пробелов: {strLength}")
```
[![img5.png](https://i.postimg.cc/WpDXKFdV/img5.png)](https://postimg.cc/RqB7J01p)
