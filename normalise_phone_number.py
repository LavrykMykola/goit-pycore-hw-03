import re #Імпортуємо бібліотеку

def normalize_phone(phone_number):
    pattern = r"\D"
    replacement = ""
    formatted_number = re.sub(pattern, replacement, phone_number) #Видаляємо усі символи окрім цифр
    if len(formatted_number) >= 10:
        formatted_number = formatted_number[-10:]
    formatted_number = "+38" + formatted_number #Додаємо префікс +38 до усіх номерів
    return formatted_number #Повертаємо готовий номер телефону
