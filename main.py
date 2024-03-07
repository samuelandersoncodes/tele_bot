import telebot
from env import TELEGRAM_BOT_TOKEN

bot = telebot(TELEGRAM_BOT_TOKEN, parse_mode=None)

bot.polling()