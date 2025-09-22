firstNumber = input("Введите первое число: ").replace(",", ".")
secondNumber = input("Введите второе число: ").replace(',', '.')

summary = float(firstNumber) + float(secondNumber)
avg = (summary / 2 )

print(f"Сумма = {summary} ; Среднее арифметическое = {avg}")