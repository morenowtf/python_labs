fullName = input("Введите ФИО: ")

uppercase = ""
for char in fullName:
    if char.isupper():
        uppercase += char

strLength = len(fullName.replace(" ", ""))

print(f"Инициалы: {uppercase} \nКоличество символов без пробелов: {strLength}")