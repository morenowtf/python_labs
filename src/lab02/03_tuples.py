def format_record(rec: tuple[str, str, float]) -> str:
    fio, group, gpa = rec
    
    if not fio or not fio.strip():
        raise ValueError("ФИО не может быть пустым")
    if not group or not group.strip():
        raise ValueError("Группа не может быть пустой")
    if not isinstance(gpa, (int, float)):
        raise TypeError("GPA должно быть числом")
    
    fio_parts = ' '.join(fio.split()).title().split()
    
    if len(fio_parts) == 3:
        initials = f"{fio_parts[1][0]}.{fio_parts[2][0]}."
    elif len(fio_parts) == 2:
        initials = f"{fio_parts[1][0]}."
    else:
        raise ValueError("ФИО должно содержать 2 или 3 части")
    
    formatted_gpa = f"{gpa:.2f}"
    
    return f"{fio_parts[0]} {initials}, гр. {group.strip()}, GPA {formatted_gpa}"

# Тесты
print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))