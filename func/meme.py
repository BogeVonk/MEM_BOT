from init_bot import bot


def process_button_callback_meme(message):
    if message.text == '2017':
        bot.reply_to(message, "Мемы 2017:")

        bot.send_photo(message.chat.id, photo=open("handlers/photo 2017/1.jpg", 'rb'))
        bot.send_photo(message.chat.id, photo=open("handlers/photo 2017/2.webp", 'rb'))
        bot.send_photo(message.chat.id, photo=open("handlers/photo 2017/3.webp", 'rb'))
        bot.send_photo(message.chat.id, photo=open("handlers/photo 2017/4.webp", 'rb'))
        bot.send_photo(message.chat.id, photo=open("handlers/photo 2017/5.webp", 'rb'))
        bot.send_photo(message.chat.id, photo=open("handlers/photo 2017/6.webp", 'rb'))

    elif message.text == '2018':
        bot.reply_to(message, "Мемы 2018:")

        bot.send_photo(message.chat.id, photo=open("handlers/photo 2018/1.jpg", 'rb'))
        bot.send_photo(message.chat.id, photo=open("handlers/photo 2018/2.jpg", 'rb'))
        bot.send_photo(message.chat.id, photo=open("handlers/photo 2018/3.jpg", 'rb'))
        bot.send_photo(message.chat.id, photo=open("handlers/photo 2018/4.jpg", 'rb'))
        bot.send_photo(message.chat.id, photo=open("handlers/photo 2018/5.jpg", 'rb'))

    elif message.text == '2019':
        bot.reply_to(message, "Мемы 2019:")

        bot.send_photo(message.chat.id, photo=open("handlers/photo 2019/1.webp", 'rb'))
        bot.send_photo(message.chat.id, photo=open("handlers/photo 2019/2.webp", 'rb'))
        bot.send_photo(message.chat.id, photo=open("handlers/photo 2019/3.png", 'rb'))
        bot.send_photo(message.chat.id, photo=open("handlers/photo 2019/4.png", 'rb'))

    elif message.text == '2020':
        bot.reply_to(message, "Мемы 2020:")

        bot.send_photo(message.chat.id, photo=open("handlers/photo 2020/1.jpg", 'rb'))
        bot.send_photo(message.chat.id, photo=open("handlers/photo 2020/2.png", 'rb'))
        bot.send_photo(message.chat.id, photo=open("handlers/photo 2020/3.jpg", 'rb'))
        bot.send_photo(message.chat.id, photo=open("handlers/photo 2020/4.png", 'rb'))
        bot.send_photo(message.chat.id, photo=open("handlers/photo 2020/5.jpg", 'rb'))

    elif message.text == '2021':
        bot.reply_to(message, "Мемы 2021:")

        bot.send_photo(message.chat.id, photo=open("handlers/photo 2021/1.jpeg", 'rb'))
        bot.send_photo(message.chat.id, photo=open("handlers/photo 2021/2.jpeg", 'rb'))
        bot.send_photo(message.chat.id, photo=open("handlers/photo 2021/3.jpeg", 'rb'))
        bot.send_photo(message.chat.id, photo=open("handlers/photo 2021/4.jpeg", 'rb'))

    elif message.text == '2022':
        bot.reply_to(message, "Мемы 2022:")

        bot.send_photo(message.chat.id, photo=open("handlers/photo 2022/1.jpg", 'rb'))
        bot.send_photo(message.chat.id, photo=open("handlers/photo 2022/2.jpg", 'rb'))
        bot.send_photo(message.chat.id, photo=open("handlers/photo 2022/3.jpg", 'rb'))
        bot.send_photo(message.chat.id, photo=open("handlers/photo 2022/4.jpg", 'rb'))
        bot.send_photo(message.chat.id, photo=open("handlers/photo 2022/5.jpg", 'rb'))

    else:
        bot.reply_to(message, "Мемы 2023:")

        bot.send_photo(message.chat.id, photo=open("handlers/photo 2023/1.jpg", 'rb'))
        bot.send_photo(message.chat.id, photo=open("handlers/photo 2023/2.png", 'rb'))
        bot.send_photo(message.chat.id, photo=open("handlers/photo 2023/3.jpg", 'rb'))
        bot.send_photo(message.chat.id, photo=open("handlers/photo 2023/4.png", 'rb'))
        bot.send_photo(message.chat.id, photo=open("handlers/photo 2023/5.png", 'rb'))
        bot.send_photo(message.chat.id, photo=open("handlers/photo 2023/6.jpg", 'rb'))
        bot.send_photo(message.chat.id, photo=open("handlers/photo 2023/7.jpg", 'rb'))
