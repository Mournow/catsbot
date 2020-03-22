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

    scoring_dict = {
        '4Yft9rapuUA.jpg' : {
            'meme_tag' : 'оригинал'
        },
        'e4fbc411fd693f423f4f81b96238f2ee.jpg' : {
            'meme_tag' : 'непонел'
        },
        '751926387eabb27cdef9c88ae9a39889.jpg' : {
            'meme_tag' : 'хватет меня доводить пажалуста'
        },
        '147296140219221262.jpg' : {
            'meme_tag' : 'зачем я это делал'
        },
        '4baf0a71fcbe040ac90ce8052cb9cd3e.jpg' : {
            'meme_tag' : 'я не плачу это просто секундная грусть'
        },
        'f41daf45975abbec8385f5de77323913.jpg' : {
            'meme_tag' : 'закрой пожалуйста свой ебальник и не перебивай меня'
        },
        'Lz0w4vMWYBE.jpg' : {
            'meme_tag' : 'не повышай на меня буквы слыш'
        },
        'niuercfewvf.png' : {
            'meme_tag' : 'рот свой замолчи'
        },
        'oichrjnkkem.jpg' : {
            'meme_tag' : 'оригинал'
        },
        '83f48e1d1283f713eaf448a66bc6a7e8.jpg' : {
            'meme_tag' : 'оригинал'
        },
        '9d7f64bd0c4a96b7725829bb7f705bc7.jpg' : {
            'meme_tag' : 'оригинал'
        },
        'foto-plachushchego-kota-iz-memov-2.jpg' : {
            'meme_tag' : 'оригинал'
        },
        '1577531719110948279.jpg' : {
            'meme_tag' : 'помнишь, как ты в детстве любил плюшки? Я тебе еще напеку Ты только приезжай Хоть иногда'
        },
        '93c63f05ec545f3a55ee01415331f8c2.jpg' : {
            'meme_tag' : 'только я жить не хочу'
        },
        'uJLN5Cm3sD0.jpg' : {
            'meme_tag' : 'идите в пизду никакого видео чата я сплю'
        },
        'KrsYdtW-dLE.jpg' : {
            'meme_tag' : 'почемуб ты мне не пишеш'
        },
        'IeVfGd5PNCM.jpg' : {
            'meme_tag' : 'дорогой дневник ебись оно все к хуям'
        },
        'PhTuAKGyobw.jpg' : {
            'meme_tag' : 'че ты на меня кричишь чепуршило кричала у тебя еще не выросла угомонись или тебя моя биполярка угомонит'
        },
        'HAYo-83F1YY.jpg' : {
            'meme_tag' : 'все я обидевся'
        },
        'MpFv4o0GNQQ.jpg' : {
            'meme_tag' : 'ты че быканул бля'
        },
        'psgXZ55wLZU.jpg' : {
            'meme_tag' : 'эти ваши так называемые уроки я в рот ебал'
        },
        'nJ4vx3KDYJ0.jpg' : {
            'meme_tag' : 'мам дай денюшку на пива'
        },
        'kpcfnqIIgHQ.jpg' : {
            'meme_tag' : 'грусть'
        },
        'jmUjXrQP_rU.jpg' : {
            'meme_tag' : 'капец'
        },
        's8PurQ6C3lI.jpg' : {
            'meme_tag' : 'полета счастливая жизнь'
        },
        'Wr7Pcvu_CpY.jpg' : {
            'meme_tag' : 'ща кофейку бахну и норм думаю будет'
        }
    }

    # анализ через difflib
    # def similarity(s1, s2):
    #     normalized1 = s1.lower()
    #     normalized2 = s2.lower()
    #     matcher = difflib.SequenceMatcher(None, normalized1, normalized2)
    #     return matcher.ratio()

    # коэффициент танимото
    def tanimoto(s1, s2):
        a, b, c = len(s1), len(s2), 0.0

        for sym in s1:
            if sym in s2:
                c += 1

        return c / (a + b - c)

    def send_cat(url):
        try:
            path = os.path.join(os.path.abspath(os.curdir), "cats/" + url)
            img = open(path, 'rb')

            bot.send_photo(message.chat.id, img, caption="Держи котичка.", reply_to_message_id=message.message_id)
        except FileNotFoundError:
            print("Не могу найти " + url)
        except: 
            print("Другая ошибка.")

    # общие результаты скоринга
    scoring_scores = []

    def clear(strx):
        strx = strx.replace(" ", "")
        strx = strx.replace(",", "")
        strx = strx.replace(".", "")
        strx = strx.replace(":", "")
        strx = strx.replace("-", "")
        return strx


    # скоринг
    for url in scoring_dict.keys():
        score = tanimoto(clear(scoring_dict[url]['meme_tag']), clear(message.text))
        scoring_dict[url]['scoring'] = score
        scoring_scores.append(score)

    # выберем 3 макс.
    scoring_scores.sort(reverse=True)
    max1 = scoring_scores[0]
    max2 = scoring_scores[1]
    max3 = scoring_scores[2]

    if max1 == max2: max2 = ""
    if max2 == max1: max1 = ""
    if max1 == max3: max3 = ""
    if max2 == max3: max2 = ""

    for url in scoring_dict.keys():
        if scoring_dict[url]['scoring'] == max1: max1 = url
        if scoring_dict[url]['scoring'] == max2: max2 = url
        if scoring_dict[url]['scoring'] == max3: max3 = url

    send_cat(max1)
    print(max1)
    send_cat(max2)
    print(max2)
    send_cat(max3)
    print(max3)

bot.polling()


