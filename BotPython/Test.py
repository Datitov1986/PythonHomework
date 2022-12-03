import telebot
from telebot import types
from config import token
from bs4 import BeautifulSoup
import requests

bot = telebot.TeleBot(token)


def weather():
    url = 'https://yandex.com.am/weather/?lat=55.75581741&lon=37.61764526'
    response = requests.get(url)
    bs = BeautifulSoup(response.text, "lxml")
    return (bs.find('h1', 'title title_level_1 header-title__title').text + '\n' +
            bs.find('span', 'temp__value temp__value_with-unit').text + '°C, ' +
            bs.find('div', 'link__condition day-anchor i-bem').text + '\nВетер: ' +
            bs.find('span', 'wind-speed').text + ' ' + bs.find('span', 'fact__unit').text + '\n' +
            bs.find('div', 'term term_orient_h fact__feels-like').text + '°C')


def test_goroscop(message):
    markup = types.InlineKeyboardMarkup(row_width=5)
    item1 = types.InlineKeyboardButton("♈ Овен", callback_data='1')
    item2 = types.InlineKeyboardButton("♉ Телец", callback_data='2')
    item3 = types.InlineKeyboardButton("♊ Близнецы", callback_data='3')
    item4 = types.InlineKeyboardButton("♋ Рак", callback_data='4')
    item5 = types.InlineKeyboardButton("♌ Лев", callback_data='5')
    item6 = types.InlineKeyboardButton("♍ Дева", callback_data='6')
    item7 = types.InlineKeyboardButton("♎ Весы", callback_data='7')
    item8 = types.InlineKeyboardButton("♏ Скорпион", callback_data='8')
    item9 = types.InlineKeyboardButton("♐ Стрелец", callback_data='9')
    item10 = types.InlineKeyboardButton("♑ Козерог", callback_data='10')
    item11 = types.InlineKeyboardButton("♒ Водолей", callback_data='11')
    item12 = types.InlineKeyboardButton("♓ Рыбы", callback_data='12')
    markup.add(item1)
    markup.add(item2)
    markup.add(item3)
    markup.add(item4)
    markup.add(item5)
    markup.add(item6)
    markup.add(item7)
    markup.add(item8)
    markup.add(item9)
    markup.add(item10)
    markup.add(item11)
    markup.add(item12)
    bot.send_message(message.chat.id, 'Выберете знак задиака', reply_markup=markup)


def goroscop(message_text):
    if message_text == '1':
        url = 'https://horo.mail.ru/prediction/aries/tomorrow/'
    if message_text == '2':
        url = 'https://horo.mail.ru/prediction/taurus/tomorrow/'
    if message_text == '3':
        url = 'https://horo.mail.ru/prediction/gemini/tomorrow/'
    if message_text == '4':
        url = 'https://horo.mail.ru/prediction/cancer/tomorrow/'
    if message_text == '5':
        url = 'https://horo.mail.ru/prediction/leo/tomorrow/'
    if message_text == '6':
        url = 'https://horo.mail.ru/prediction/virgo/tomorrow/'
    if message_text == '7':
        url = 'https://horo.mail.ru/prediction/libra/tomorrow/'
    if message_text == '8':
        url = 'https://horo.mail.ru/prediction/scorpio/tomorrow/'
    if message_text == '9':
        url = 'https://horo.mail.ru/prediction/sagittarius/tomorrow/'
    if message_text == '10':
        url = 'https://horo.mail.ru/prediction/capricorn/tomorrow/'
    if message_text == '11':
        url = 'https://horo.mail.ru/prediction/aquarius/tomorrow/'
    if message_text == '12':
        url = 'https://horo.mail.ru/prediction/pisces/tomorrow/'
    response = requests.get(url)
    bs = BeautifulSoup(response.text, "lxml")
    return bs.find('div', 'article__item article__item_alignment_left article__item_html').text


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет ✌️я телеграм бот, звездочет ")
    bot.send_message(message.chat.id, "для использования моих функций нажми /button")


@bot.message_handler(commands=['button'])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Погода в Москве")
    item2 = types.KeyboardButton("Гороскоп")
    markup.add(item1)
    markup.add(item2)
    bot.send_message(message.chat.id, 'Выберите что вам надо', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def message_reply(message):
    if message.text == "Погода в Москве":
        bot.send_message(message.chat.id, weather())
    elif message.text == "Гороскоп":
        bot.send_message(message.chat.id, test_goroscop(message))


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        bot.send_message(call.message.chat.id, text=goroscop(call.data))


bot.infinity_polling()
