import requests
import telebot
from extensions import APIException, Convertor
import traceback

TOKEN = "6181786355:AAGXtvKh8FIpItcq_WwEzdDS_0xUuLXMNj0"
# user name: HuschbandTest_bot
# Bot name: HuschbandTest
# URL: t.me/HuschbandTest_bot

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def start(message: telebot.types.Message):
    text = "available commands: /start /help /currencies \r\nusage example: EUR RUB 1000"
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['currencies'])
def values(message: telebot.types.Message):
    text = 'Available currencies: EUR RUB USD SAR'
    bot.reply_to(message, text)

@bot.message_handler(commands=['husband'])
def values(message: telebot.types.Message):
    text = 'Awesome'
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text'])
def converter(message: telebot.types.Message):
    input = message.text.split(' ')

    try:
        if len(input) == 3:
            answer = Convertor.get_price(*input)
        else:
            answer = 'please input "/start" or "/help" to start the conversation'

    except APIException as e:
        bot.reply_to(message, f"Error in command:\n{e}")

    except Exception as e:
        traceback.print_tb(e.__traceback__)
        bot.reply_to(message, f"Unknown error:\n{e}")

    else:
        bot.reply_to(message, answer)



bot.polling()
