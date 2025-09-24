# python_labs
# Лабораторная работа 1
### Задание 1
```python
name = input("Введите ваше имя: ")
age = int(input("Введите ваш возраст: "))

print(f"Привет, {name}! Через год тебе будет {age + 1}.")
```
![ex01](https://pasteboard.co/rrPW22EOE2RS.png)

### Задание 2
```python
firstNumber = input("Введите первое число: ").replace(",", ".")
secondNumber = input("Введите второе число: ").replace(',', '.')

summary = float(firstNumber) + float(secondNumber)
avg = (summary / 2 )

print(f"Сумма = {summary} ; Среднее арифметическое = {avg}")
```

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

### Задание 4
```python
minutes = int(input("Введите минуты: "))

hours = minutes // 60
remaining_minutes = minutes % 60

print(f"Минуты: {minutes} \n{hours}:{remaining_minutes:02d}")
```

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
