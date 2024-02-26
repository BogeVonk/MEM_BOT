from init_bot import bot


def process_button_callback_style(message):
    if message.text == '2017':
        bot.reply_to(message, "Стиль 2017 - мальчик скейтер:")

        bot.send_photo(message.chat.id, photo=open("handlers/photo 2017/2017.png", 'rb'))

    elif message.text == '2018':
        bot.reply_to(message, "Стиль 2018 - продавец К&Б:")

        bot.send_photo(message.chat.id, photo=open("handlers/photo 2018/2018.png", 'rb'))

    elif message.text == '2019':
        bot.reply_to(message, "Стиль 2019 - кринж малолетки:")

        bot.send_photo(message.chat.id, photo=open("handlers/photo 2019/2019.png", 'rb'))

    elif message.text == '2020':
        bot.reply_to(message, "Стиль 2019 - короновирус:")

        bot.send_photo(message.chat.id, photo=open("handlers/photo 2020/2020.png", 'rb'))

    elif message.text == '2021':
        bot.reply_to(message, "Стиль 2019 - оффники:")

        bot.send_photo(message.chat.id, photo=open("handlers/photo 2021/2021.png", 'rb'))

    elif message.text == '2022':
        bot.reply_to(message, "Стиль 2019 - реданы:")

        bot.send_photo(message.chat.id, photo=open("handlers/photo 2022/2022.png", 'rb'))

    else:
        bot.reply_to(message, "Стиль 2019 - слово пацана:")

        bot.send_photo(message.chat.id, photo=open("handlers/photo 2023/2023.png", 'rb'))
