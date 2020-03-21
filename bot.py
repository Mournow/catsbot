# -*- coding: utf-8 -*-
# import redis
import os
import telebot
import difflib
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

    max_similarity = { 'url': "", 'score': 0 }

    for url in scoring_dict.keys():
        scoring = similarity(scoring_dict[url]['meme_tag'], message.text)

        if scoring > max_similarity['score'] :
            max_similarity['score'] = scoring
            max_similarity['url'] = scoring_dict[url]

    img = open(os.path.join(os.path.abspath(os.curdir), max_similarity['url']), 'rb')

    bot.send_photo(message.chat.id, img, caption=max_similarity['score'], reply_to_message_id=message.message_id)

bot.polling()


scoring_dict = {
    's7zN3CUtdPA.jpg' : {
        'meme_tag' : 'здравствуйте, а вам не кажется что вы срочно должны пойти нахуй',
        'situation' : ''
    },
    'HVVmlVL2CEg.jpg' : {
        'meme_tag' : 'я вот посидел поныл и ничего не изменилось ахуеть блять',
        'situation' : ''
    },
    'fc4incnslfctis8ft3top.jpg' : {
        'meme_tag' : 'у нас есть только два союзника: цмок и кусь',
        'situation' : ''
    },
    '4Yft9rapuUA.jpg' : {
        'meme_tag' : '',
        'situation' : 'плачет'
    }
}

def similarity(s1, s2):
  normalized1 = s1.lower()
  normalized2 = s2.lower()
  matcher = difflib.SequenceMatcher(None, normalized1, normalized2)
  return matcher.ratio()