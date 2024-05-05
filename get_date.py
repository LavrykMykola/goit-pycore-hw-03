import datetime #Імпортуємо бібліотеку

def get_days_from_date(wanted_date):
    current_date = datetime.date.today() #Отримуємо поточну дату
    try:
        wanted_date = datetime.datetime.strptime(wanted_date, "%Y-%m-%d") #Конвертуємо рядок в об'єкт
        wanted_date = wanted_date.date() #Залишаємо тільки дату
    except ValueError: #Враховуємо помилку пр введенні
        print("формат рядка дати був введений неправильно! Перевірте правильність написання рядку")
    else: # Якщо без помилок - виконуємо наступне
        difference = wanted_date - current_date
        print(difference.days) #Виводимо залишок днів

get_days_from_date("2024-09-01")