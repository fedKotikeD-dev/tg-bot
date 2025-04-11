import db
import RUN_THIS
import random
import time
import requests

def random_number():
    db.number = int(random.randint(1, 100))
    while True:
        db.guess = int(input("Назовите число от 1 до 100: "))
        if db.guess == db.number:
            print("Вы угадали!")
            break
        elif db.guess < db.number:
            print("Загаданное число больше.")
        else:
            print("Загаданное число меньше.")

def calculator():
    print("Расширенный калькулятор")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("5. Возведение в степень")
    print("6. Квадратный корень")
    db.choice = int(input("Выберите операцию: "))
    db.num1 = float(input("Введите первое число: "))

    if db.choice == 1:
        db.num2 = float(input("Введите второе число: "))
        db.result = db.num1 + db.num2
        print(f"Результат: {db.result}")
    elif db.choice == 2:
        db.num2 = float(input("Введите второе число: "))
        db.result = db.num1 - db.num2
        print(f"Результат: {db.result}")
    elif db.choice == 3:
        db.num2 = float(input("Введите второе число: "))
        db.result = db.num1 * db.num2
        print(f"Результат: {db.result}")
    elif db.choice == 4:
        db.num2 = float(input("Введите второе число: "))
        if db.num2 != 0:
            db.result = db.num1 / db.num2
            print(f"Результат: {db.result}")
        else:
            print("Ошибка: Деление на ноль.")
    elif db.choice == 5:
        db.result = db.num1 ** 2
        print(f"Результат: {db.result}")
    elif db.choice == 6:
        if db.num1 >= 0:
            db.result = db.num1 ** 0.5
            print(f"Результат: {db.result}")
        else:
            print("Ошибка: Квадратный корень из отрицательного числа.")
    else:
        print("Неверный выбор операции.")

def investment_calculator():
    print("Калькулятор дохода от инвестиций")
    db.principal = float(input("Введите стартовую сумму (начальный капитал): "))
    db.rate = float(input("Введите годовую процентную ставку (в %): "))
    db.years = int(input("Введите срок вклада (в годах): "))
    db.final_amount = db.principal * (1 + db.rate / 100) ** db.years
    db.profit = db.final_amount - db.principal
    print(f"Итоговая сумма: {db.final_amount:.2f}")
    print(f"Чистая прибыль: {db.profit:.2f}")

def get_weather(city):
    db.api_key = "d82c2b1bba01da54d351029ec7d961e6"  # Замените на ваш API-ключ OpenWeather
    db.base_url = "http://api.openweathermap.org/data/2.5/weather"
    db.params = {
        "q": db.city,
        "appid": db.api_key,
        "units": "metric",  # Используем градусы Цельсия
        "lang": "ru"       # Локализация на русский язык
    }

    try:
        db.response = requests.get(db.base_url, params=db.params)
        db.data = db.response.json()

        if db.response.status_code == 200:
            db.city_name = db.ata["name"]
            db.temp = db.data["main"]["temp"]
            db.weather_desc = db.data["weather"][0]["description"]
            return f"Погода в {db.city_name}: {db.temp}°C, {db.weather_desc.capitalize()}."
        else:
            return f"Ошибка: {db.data['message']}"
    except Exception as e:
        return f"Не удалось получить данные о погоде: {e}"
    
def menu():
    print("1. Игра 'Угадай число'")
    print("2. Калькулятор")
    print("3. Финансовый калькулятор")
    print("4. Прогноз погоды")
    print("3. Выход")
    choice = int(input("Выберите пункт меню: "))
    if choice == 1:
        random_number()
    elif choice == 2:
        calculator()
    elif choice == 3:
        investment_calculator()
    elif choice == 4:   
        db.city = input("Введите название города: ")
        db.weather_info = get_weather(db.city)
        print(db.weather_info)
    elif choice == 5:
        print("Выход из программы.")
        exit()
    else:
        print("Неверный выбор. Попробуйте снова.")
        time.sleep(2)
        menu()