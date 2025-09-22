price = float(input("Введите цену: "))
discount = float(input("Введите процент скидки: "))
vat = float(input("Введите процент налогов: "))

base = price * (1 - discount / 100)
vat_amount = base * (vat/100)
total = base + vat_amount

print(f"База после скидки: {base} \nНДС: {vat_amount} \nИтого к оплате: {total}")
#База после скидки: 900.00 ₽
#НДС:               180.00 ₽
#Итого к оплате:    1080.00 ₽