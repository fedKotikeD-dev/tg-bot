import db
import random
import time
import requests
import telebot as tg
bot = tg.TeleBot('ne skazhy')

db.number = int(random.randint(1, 100))
@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/random':
        bot.send_message(message.from_user.id, "Назовите число от 1 до 100")
        bot.register_next_step_handler(message, say_answer_number)
    elif message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Имеющиеся на данный момент команды:")
        time.sleep(0.1)
        bot.send_message(message.from_user.id, "Привет - поздороваться с ботом")
        time.sleep(0.1)
        bot.send_message(message.from_user.id, "/random - игра в угадывание числа")
        time.sleep(0.1)
        bot.send_message(message.from_user.id, "/help - эта команда")
        time.sleep(0.1)
        bot.send_message(message.from_user.id, "/calc - продвинутый калькулятор")
        time.sleep(0.1)
        bot.send_message(message.from_user.id, "/invest - калькулятор вклада")
        time.sleep(0.1)
        bot.send_message(message.from_user.id, "/weather - погода в указанном городе")
        time.sleep(0.1)
        bot.send_message(message.from_user.id, "/start - начальное приветствие бота")
    elif message.text == '/calc':
        bot.send_message(message.from_user.id, "Возможные операции:")
        time.sleep(0.1)
        bot.send_message(message.from_user.id, "1. Сложение")
        time.sleep(0.1)
        bot.send_message(message.from_user.id, "2. Вычитание")
        time.sleep(0.1)
        bot.send_message(message.from_user.id, "3. Умножение.")
        time.sleep(0.1)
        bot.send_message(message.from_user.id, "4. Деление")
        time.sleep(0.1)
        bot.send_message(message.from_user.id, "5. Возведение в квадрат")
        time.sleep(0.1)
        bot.send_message(message.from_user.id, "6. Квадратный корень")
        time.sleep(0.1)
        bot.send_message(message.from_user.id, "Укажите номер операции")
        bot.register_next_step_handler(message, calculator1)
    elif message.text == '/invest':
        bot.send_message(message.from_user.id, "Введите ваш стартовый капитал")
        bot.register_next_step_handler(message, invest1)
    elif message.text == "/weather":
        bot.send_message(message.from_user.id, "Укажите город для определения погоды")
        bot.register_next_step_handler(message, weather)
    elif message.text == "/start":
        bot.send_message(message.from_user.id, "Привет! Я бот-помощник, обладающий интересными функциями. Со списком команд ты можешь ознакомиться в /help.")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
def say_answer_number(message):
    try:
        db.guess = int(message.text)
    except ValueError:
        bot.send_message(message.from_user.id, "Пожалуйста, введите корректное число.")
        return
    if db.guess == db.number:
        bot.send_message(message.from_user.id, "Вы угадали!")
        db.number = int(random.randint(1, 100))
    elif db.guess < db.number:
        bot.send_message(message.from_user.id, "Загаданное число больше!")
        time.sleep(0.1)
        start()
    elif db.guess > db.number:
        bot.send_message(message.from_user.id, "Загаданное число меньше!")
        time.sleep(0.1)
        start()
def calculator1(message):
    db.choice = int(message.text)
    bot.send_message(message.from_user.id, "Укажите первое число")
    bot.register_next_step_handler(message, calculator2)
def calculator2(message):
    db.num1 = int(message.text)
    if db.choice == 1:
        bot.send_message(message.from_user.id, "Укажите второе число")
        bot.register_next_step_handler(message, calculator_plus)
    elif db.choice == 2:
        bot.send_message(message.from_user.id, "Укажите второе число")
        bot.register_next_step_handler(message, calculator_minus)
    elif db.choice == 3:
        bot.send_message(message.from_user.id, "Укажите второе число")
        bot.register_next_step_handler(message, calculator_multiplication)
    elif db.choice == 4:
        bot.send_message(message.from_user.id, "Укажите второе число")
        bot.register_next_step_handler(message, calculator_division)
    elif db.choice == 5:
        db.result = db.num1 ** 2
        bot.send_message(message.from_user.id, f'{db.num1} в квадрате будет равно {db.result}')
    elif db.choice == 6:
        if db.num1 >= 0:
            db.result = db.num1 ** 0.5
            bot.send_message(message.from_user.id, f'Корень из {db.num1} будет равен {db.result}')
        else:
            bot.send_message(message.from_user.id, "Корня из отрицательного числа не существует")
    else:
        bot.send_message(message.from_user.id, "Возникла ошибка при выборе операции. Попробуйте снова.")
def calculator_plus(message):
    db.num2 = int(message.text)
    db.result = db.num1 + db.num2
    bot.send_message(message.from_user.id, f'{db.num1} + {db.num2} = {db.result}')
def calculator_minus(message):
    db.num2 = int(message.text)
    db.result = db.num1 - db.num2
    bot.send_message(message.from_user.id, f'{db.num1} - {db.num2} = {db.result}')
def calculator_multiplication(message):
    db.num2 = int(message.text)
    db.result = db.num1 * db.num2
    bot.send_message(message.from_user.id, f'{db.num1} * {db.num2} = {db.result}')
def calculator_division(message):
    db.num2 = int(message.text)
    if db.num2 != 0:
        db.result = db.num1 / db.num2
        bot.send_message(message.from_user.id, f'{db.num1} : {db.num2} = {db.result}')
    else:
        bot.send_message(message.from_user.id, "Делить на ноль нельзя!")
def invest1(message):
    db.principal = float(message.text)
    if db.principal >= 0:
        bot.send_message(message.from_user.id, "Введите годовую процентную ставку (в %)")
        bot.register_next_step_handler(message, invest2)
    else:
        bot.send_message(message.from_user.id, "Стартовый капитал не может быть меньше 0.")
def invest2(message):
    db.rate = float (message.text)
    if db.rate >= 0:
        bot.send_message(message.from_user.id, "Введите срок вклада (в годах)")
        bot.register_next_step_handler(message, invest3)
    else:
        bot.send_message(message.from_user.id, "Во вкладе не может быть отрицательный процент.")
def invest3(message):
    db.years = float(message.text)
    if db.years >= 0:
        db.final_amount = db.principal * (1 + db.rate / 100) ** db.years
        db.profit = db.final_amount - db.principal
        bot.send_message(message.from_user.id, f'Вы получите {db.final_amount:.2f}')
        time.sleep(0.1)
        bot.send_message(message.from_user.id, f'Чистая прибыль: {db.profit:.2f}')
    else:
        bot.send_message(message.from_user.id, "Не может быть отрицательное количество лет.")
def weather(message):
    db.city = message.text
    db.api_key = "d82c2b1bba01da54d351029ec7d961e6"
    db.base_url = "http://api.openweathermap.org/data/2.5/weather"
    db.params = {
        "q": db.city,
        "appid": db.api_key,
        "units": "metric",
        "lang": "ru"
    }
    try:
        db.response = requests.get(db.base_url, params=db.params)
        db.data = db.response.json()
        if db.response.status_code == 200:
            db.city_name = db.data["name"]
            db.temp = db.data["main"]["temp"]
            db.weather_desc = db.data["weather"][0]["description"]
            bot.send_message(message.from_user.id, f'Погода в {db.city_name}: {db.temp}°C, {db.weather_desc.capitalize()}')
        else:
            bot.send_message(message.from_user.id, f'Ошибка: {db.data['message']}')
    except Exception as e:
        bot.send_message(message.from_user.id, f'Не удалось получить данные о погоде.')

bot.polling(none_stop=True, interval=0)