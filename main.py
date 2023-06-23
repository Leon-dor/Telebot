import telebot
from telebot import types
import random
import datetime
import logging
import SigmaRules_sending
import time

bot = telebot.TeleBot("6156730475:AAFUHqGhJscVxcux6DM1EKguGMH25ABFVJ8")

photos = ["BN-HA234_0315BW_16H_20150218155250.jpg", "EwPlegAWgAQh15U.jpg", "pedro-moreno-shirtless-2560x1920.jpg",
          "rBVaqWCJYXaAShGqAADvzjLDi3U591.jpg",
          "RClOFRCWxWNnHuUdHerLlHfSz6riI1lOdgEZPoAAKdORrPelY_ofm-h-CFPJHc7cF-nUbl47.jpg"]

sigma_channel = "https://youtube.com/shorts/UCT0OARvv0-VeRZMUNW_e9hw"


logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)


@bot.message_handler(commands=["start"])
def start(message):
    mess = f"Welcome to the club <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>"
    mess_2 = f"Welcome to the club <b>{message.from_user.first_name}</b>"
    if message.from_user.last_name is None:
        bot.send_message(message.chat.id, mess_2, parse_mode="html")
    else:
        bot.send_message(message.chat.id, mess, parse_mode="html")


@bot.message_handler(content_types=["text"])
def get_user_text(message):
    if message.text.lower() == "hello" or message.text.lower() == "hi":
        bot.send_message(message.chat.id, "Hi!", parse_mode="html")
    elif message.text.lower() == "photo":
        photo = open(random.choice(photos), "rb")
        bot.send_photo(message.chat.id, photo)
    elif message.text.lower() == "id":
        bot.send_message(message.chat.id, f"Your ID: {message.from_user.id}")


@bot.message_handler(content_types=["photo"])
def get_user_photo(message):
    bot.send_message(message.chat.id, "I'm blind, but if there's your cock, then I say nice cock!")


@bot.message_handler(commands=["website"])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Visit based website", url=sigma_channel))
    bot.send_message(message.chat.id, "You can visit website", reply_markup=markup)


@bot.message_handler(commands=["help"])
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    websites = types.KeyboardButton("/website")
    starting = types.KeyboardButton("/start")

    markup.add(websites, starting)
    markup.add(types.InlineKeyboardButton("Visit website", url=sigma_channel))
    bot.send_message(message.chat.id, sigma_channel, reply_markup=markup)


@bot.message_handler(commands=["mess"])
def mess(message):

    bot.send_message(message.chat.id, "Hello Bitches")


@bot.message_handler()
def start(message):
    while True:
        now = datetime.datetime.now()
        now_time = now.strftime('%H:%M')
        if now_time == "12:30":
            is_finishing = False
        while not is_finishing:
            mess = SigmaRules_sending.sigma_rules()
            # time.sleep()
            # now_time == "15:41":
            bot.send_message(message.chat.id, mess, parse_mode="html")
            if now_time == "12:32":
                is_finishing = True


bot.polling(none_stop=True)
