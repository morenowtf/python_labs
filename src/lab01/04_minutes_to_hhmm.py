minutes = int(input("Введите минуты: "))

days = minutes // (24 * 60)
remaining_minutes_after_days = minutes % (24 * 60)
hours = remaining_minutes_after_days // 60
remaining_minutes = remaining_minutes_after_days % 60

if days > 0:
    print(f"Минуты: {minutes} \n{days} сутки, {hours}:{remaining_minutes:02d}")
else:
    print(f"Минуты: {minutes} \n{hours}:{remaining_minutes:02d}")