import telebot

from func.date_time import get_welcome
from func.meme import process_button_callback_meme
from func.style import process_button_callback_style
from init_bot import bot


@bot.message_handler(commands=["start", "help"])
def start_help(message: telebot.types.Message):
    text1 = (f"{get_welcome()} Я шарящий бот)\n"
             f"Я покажу тебе, за что ты должкн шарить!\n"
             f"/meme - Мемы\n"
             f"/style - Стиль одежды\n")
    bot.send_message(message.chat.id, text1)


@bot.message_handler(commands=["meme"])
def years(message: telebot.types.Message):
    markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
    button1 = telebot.types.KeyboardButton("2017")
    button2 = telebot.types.KeyboardButton("2018")
    button3 = telebot.types.KeyboardButton("2019")
    button4 = telebot.types.KeyboardButton("2020")
    button5 = telebot.types.KeyboardButton("2021")
    button6 = telebot.types.KeyboardButton("2022")
    button7 = telebot.types.KeyboardButton("2023")
    markup.add(button1, button2, button3, button4, button5, button6, button7)
    msg = bot.send_message(message.chat.id, 'Выберите кнопку:', reply_markup=markup)
    bot.register_next_step_handler(msg, process_button_callback_meme)


@bot.message_handler(commands=["style"])
def years(message: telebot.types.Message):
    markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
    button1 = telebot.types.KeyboardButton("2017")
    button2 = telebot.types.KeyboardButton("2018")
    button3 = telebot.types.KeyboardButton("2019")
    button4 = telebot.types.KeyboardButton("2020")
    button5 = telebot.types.KeyboardButton("2021")
    button6 = telebot.types.KeyboardButton("2022")
    button7 = telebot.types.KeyboardButton("2023")
    markup.add(button1, button2, button3, button4, button5, button6, button7)
    msg = bot.send_message(message.chat.id, 'Выберите кнопку:', reply_markup=markup)
    bot.register_next_step_handler(msg, process_button_callback_style)
