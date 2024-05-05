import random #Імпортуємо бібліотеку

def get_numbers_ticket(min, max, quantity):
    list_of_numbers = [] #Створюємо пустий список
    while len(list_of_numbers) < quantity: #Виконуємо цикл поки розмір списку не буде дорівнювати quantity
        random_number = random.randint(min, max)
        if any(i == random_number for i in list_of_numbers): #Якщо згенероване число не унікальне - то пропускаємо його
            continue
        else:
            list_of_numbers.append(random_number)
    list_of_numbers.sort() #Сортуємо отриманий список
    return list_of_numbers #Повертаємо відсортований список

try:
    min_value = int(input("Введіть мінімальне ціле число від 1 до 1000: "))
    max_value = int(input("Введіть максимальне ціле число від 1 до 1000: "))
except ValueError:
    print("Ви ввели число яке не підлежить умовам!")
else:
    if min_value > max_value:
        print("Мінімальне число більше за максимальне!")
    elif min_value == max_value:
        print("Мінімальне та максимальне числа однакові!")
    elif min_value < 1 or max_value > 1000:
        print("Числа виходять за межі!")
    else:
        quantity = random.randint(1, max_value - min_value) #Отримуємо випадкову кількість виграшних чисел
        lottery_numbers = get_numbers_ticket(min_value, max_value, quantity) #Викликаємо функцію та отримуємо список чисел
        print("Ваші лотерейні числа:", lottery_numbers)