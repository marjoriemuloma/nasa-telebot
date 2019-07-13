import telebot
import config
import json


bot = telebot.TeleBot(config.telegram_api_key)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(
    message, "Hello, I am from NASA, I can send you a daily image if you reply with /nasa",
    )

@bot.message_handler(commands=['nasa'])
def send_welcome(message):
    import requests
    image = requests.get(config.nasa_url)
    image_text = image.text
    data = json.loads(image_text)
    image_date = data["date"]
    image_title = data["title"]
    image_url = data["url"]
    image_date = data["date"]
    image_explanation = data["explanation"]

    bot.reply_to(
    message, image_title + "👉" + image_explanation + " " + image_url ,
    )

bot.polling()
