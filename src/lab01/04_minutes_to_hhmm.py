minutes = int(input("Введите минуты: "))

hours = minutes // 60
remaining_minutes = minutes % 60

print(f"Минуты: {minutes} \n{hours}:{remaining_minutes:02d}")