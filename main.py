import telebot
from env import TELEGRAM_BOT_TOKEN

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN, parse_mode=None)


@bot.message_handler(commands=["help", "hello"])
def send_help(message):
    bot.reply_to(message, "Hello, auto bot here!")


bot.polling()
