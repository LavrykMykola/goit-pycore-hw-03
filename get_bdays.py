import datetime #Імпортуємо бібліотеку

def get_upcoming_birthdays(list_of_users):
    close_birthdays = [] #Створюємо пустий список для днів народження
    today = datetime.datetime.today().date() #Отримуємо сьогоднішню дату
    curr_year = datetime.datetime.today().year #Окремо задаємо об'єкт року для подальшої заміни року
    for user in list_of_users: 
        bday = datetime.datetime.strptime(user["birthday"], "%Y.%m.%d").date() #Створюємо об'єкт дати дня народження
        bday_this_year = bday.replace(year = curr_year) #Замінюємо рік на поточний
        difference = bday_this_year - today #Знаходимо, наскільки далеко день народження
        day_of_week = bday_this_year.weekday() #Знаходимо, на який день тижня припадає день народження
        if 0 <= difference.days <= 7 and day_of_week != 5 and day_of_week != 6: #Якщо день народження під час наступнього тижня, та не припадає на вихідні:
            bday_celebration = bday_this_year.strftime("%Y.%m.%d") #Робимо з об'єкта рядок
            close_birthdays.append({"name": user["name"], "birthday_celebration": bday_celebration}) #Створюємо та додаємо словник до списку
        elif 0 <= difference.days <= 7 and day_of_week == 5: #Якщо день припадає на субботу:
            bday_celebration = bday_this_year.replace(day = bday_this_year.day + 2).strftime("%Y.%m.%d") #Переносимо дату на два дні, та робимо рядок
            close_birthdays.append({"name": user["name"], "birthday_celebration": bday_celebration}) #Створюємо та додаємо словник до списку
        elif 0 <= difference.days <= 7 and day_of_week == 6: #Якщо день припадає на неділю:
            bday_celebration = bday_this_year.replace(day = bday_this_year.day + 1).strftime("%Y.%m.%d") #Переносимо дату на один день, та робимо рядок
            close_birthdays.append({"name": user["name"], "birthday_celebration": bday_celebration}) #Створюємо та додаємо словник до списку
    return close_birthdays #Повертаємо готовий список словників найближчих днів народження
    

users = [
    {"name": "John Doe", "birthday": "1985.05.04"},
    {"name": "Jane Smith", "birthday": "1990.05.05"},
    {"name": "Smbdy1", "birthday": "1986.02.14"},
    {"name": "Smbdy2", "birthday": "1999.05.08"},
    {"name": "Smbdy3", "birthday": "2001.05.10"},
    {"name": "Smbdy4", "birthday": "1959.05.04"},
]
print(get_upcoming_birthdays(users))