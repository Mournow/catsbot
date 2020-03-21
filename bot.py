# -*- coding: utf-8 -*-
# import redis
import os
import telebot
# import some_api_lib
# import ...

# Example of your code beginning
#           Config vars
token = os.environ['TELEGRAM_TOKEN']
some_api_token = os.environ['SOME_API_TOKEN']
#             ...

# If you use redis, install this add-on https://elements.heroku.com/addons/heroku-redis
# r = redis.from_url(os.environ.get("REDIS_URL"))

#       Your bot code below
bot = telebot.TeleBot(token)
# some_api = some_api_lib.connect(some_api_token)
#              ...


@bot.message_handler(commands=['дайкота'])

def start_message(message):
    img = open('cats\\s7zN3CUtdPA.jpg', 'rb')

    bot.send_photo(message.chat.id, img, reply_to_message_id=message.chat.id)

bot.polling()