import pyttsx3
import telebot
import requests
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

engin = pyttsx3.init()

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
    bot.send_message(message.chat.id, "Привет! Я бот, который озвучивает прогноз погоды")

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


bot.polling()