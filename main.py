import pyttsx3
import telebot
import requests
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

engin = pyttsx3.init()

he = ['/start', '/help', '/weather', '/F', '/C']

def get_weather(city):
    url = f"https://wttr.in/{city}?format=%C+%t"
    responce = requests.get(url)

    if responce.status_code == 200:
        return responce.text.strip()
    else:
        return "Не удалось получить данные о погоде. Попробуйте позже."
    
def speak(text):
    engin.say(text)
    engin.runAndWait()

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я бот, который озвучивает прогноз погоды и не только😏")
@bot.message_handler(commands=["help"])
def start(message):
    bot.send_message(message.chat.id, "Вот мои команды:")
    for i in he:
        bot.send_message(message.chat.id, i)

@bot.message_handler(commands=["weather"])
def weather(message):
    words = message.text.split(maxsplit=1)
    if len(words) < 2:
        bot.send_message(message.chat.id, "Пожалуйста, укажи город. Пример: /weather London")
        return
    city = words[1]
    weather_info = get_weather(city)
    answer = f"Погода в {city}: {weather_info}"
    bot.send_message(message.chat.id,  answer)
    speak(answer)
@bot.message_handler(commands=["F"])
def weather(message):
    words = message.text.split(maxsplit=1)
    if len(words) < 2:
        bot.send_message(message.chat.id, "Пожалуйста, укажи сколько градусов по Фаренгейту перевести в градусы по Цельсию. Пример: /F 32.0")
        return
    f = float(words[1])
    temp = (f - 32) * (5/9)
    answer = f"Температура в градусах по Цельсию: {temp}"
    bot.send_message(message.chat.id,  answer)
    speak(answer)
@bot.message_handler(commands=["C"])
def weather(message):
    words = message.text.split(maxsplit=1)
    if len(words) < 2:
        bot.send_message(message.chat.id, "Пожалуйста, укажи сколько градусов по Цельсию перевести в градусы по Фаренгейту. Пример: /С 2")
        return
    c = float(words[1])
    temp = (c * (9/5)) + 32 
    answer = f"Температура в градусах по Фаренгейту: {temp}"
    bot.send_message(message.chat.id,  answer)
#    speak(answer) :(

bot.polling()