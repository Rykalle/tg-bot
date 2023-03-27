
import telebot
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from poisk import *
bot = telebot.TeleBot('6160559595:AAEd4FqAfDYZ4iGWYgRSRQty9tkykZLUhCU')
poisk_filtr = []
try:
	from googlesearch import search
except ImportError:
	print("No module named 'google' found")

def poisk(query):
	# to search
	#query = "Geeksforgeeks"

	for j in search(query, tld="co.in", num=10, stop=10, pause=2):
		print(j)

# print(poisk(input()))
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Начнём!")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "Начнём?", reply_markup=markup)
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Начнём!":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("5 лет")
            btn2 = types.KeyboardButton("6 лет")
            btn3 = types.KeyboardButton("7 лет")
            btn4 = types.KeyboardButton("8 лет")
            btn5 = types.KeyboardButton("9 лет")
            btn6 = types.KeyboardButton("10 лет")
            btn7 = types.KeyboardButton("11 лет")
            btn8 = types.KeyboardButton("12 лет")
            btn9 = types.KeyboardButton("13 лет")
            btn10 = types.KeyboardButton("14 лет")
            btn11 = types.KeyboardButton("15 лет")
            btn12 = types.KeyboardButton("16 лет")
            btn13 = types.KeyboardButton("17 лет")
            btn14 = types.KeyboardButton("18 лет")
            markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12, btn13, btn14)
            bot.send_message(message.from_user.id, "Привет! Сколько тебе лет?", reply_markup=markup)
    elif (message.text in ['5 лет', '6 лет', '7 лет', '8 лет', '9 лет', '10 лет', '11 лет', '12 лет', '18 лет', '13 лет', '14 лет', '15 лет', '16 лет', '17 лет']):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('Заочно')
            btn2 = types.KeyboardButton('Очно')
            markup.add(btn1, btn2)
            bot.send_message(message.from_user.id, 'Как вы будете обучаться?', reply_markup=markup)
    elif (message.text == 'Очно'):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('Владимир')
            btn2 = types.KeyboardButton('Александров')
            btn3 = types.KeyboardButton('Вязанки')
            btn4 = types.KeyboardButton('Гороховец')
            btn5 = types.KeyboardButton('Ковров')
            btn6 = types.KeyboardButton('Суздаль')
            markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
            bot.send_message(message.from_user.id, 'Укажите ваш город', reply_markup=markup)
    elif message.text in ['Владимир', 'Суздаль', 'Гороховец', 'Вязники', 'Ковров', 'Александров']:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('Январь')
            btn2 = types.KeyboardButton('Февраль')
            btn3 = types.KeyboardButton('Март')
            btn4 = types.KeyboardButton('Апрель')
            btn5 = types.KeyboardButton('Май')
            btn6 = types.KeyboardButton('Июнь')
            btn7 = types.KeyboardButton('Июль')
            btn8 = types.KeyboardButton('Август')
            btn9 = types.KeyboardButton('Сентябрь')
            btn10 = types.KeyboardButton('Октябрь')
            btn11 = types.KeyboardButton('Ноябрь')
            btn12 = types.KeyboardButton('Декабрь')
            markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12)
            bot.send_message(message.from_user.id, 'Укажите месяц начала обучения', reply_markup=markup)
    elif message.text == 'Заочно':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('Январь')
            btn2 = types.KeyboardButton('Февраль')
            btn3 = types.KeyboardButton('Март')
            btn4 = types.KeyboardButton('Апрель')
            btn5 = types.KeyboardButton('Май')
            btn6 = types.KeyboardButton('Июнь')
            btn7 = types.KeyboardButton('Июль')
            btn8 = types.KeyboardButton('Август')
            btn9 = types.KeyboardButton('Сентябрь')
            btn10 = types.KeyboardButton('Октябрь')
            btn11 = types.KeyboardButton('Ноябрь')
            btn12 = types.KeyboardButton('Декабрь')
            markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12)
            bot.send_message(message.from_user.id, 'Укажите месяц начала обучения', reply_markup=markup)
    elif message.text in ['Январь', 'Февраль', 'Декабрь', 'Март', 'Апрель', 'Май', 'Ноябрь', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь']:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('1')
            btn2 = types.KeyboardButton('2')
            btn3 = types.KeyboardButton('3')
            btn4 = types.KeyboardButton('4')
            btn5 = types.KeyboardButton('5')
            btn6 = types.KeyboardButton('6')
            btn7 = types.KeyboardButton('7')
            btn8 = types.KeyboardButton('8')
            btn9 = types.KeyboardButton('9')
            btn10 = types.KeyboardButton('10')
            markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10)
            bot.send_message(message.from_user.id, 'Укажите интересующий вас рейтинг курса', reply_markup=markup)
    elif message.text in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('С ОВЗ')
            btn2 = types.KeyboardButton('Без ОВЗ')
            markup.add(btn1, btn2)
            bot.send_message(message.from_user.id, 'Должен ли курс поддержвать ОВЗ?', reply_markup=markup)
    elif message.text in ['С ОВЗ', 'Без ОВЗ']:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('Платно')
            btn2 = types.KeyboardButton('Бесплатно')
            markup.add(btn1, btn2)
            bot.send_message(message.from_user.id, 'Готовы ли вы заплатить?', reply_markup=markup)
    elif message.text in ['Платно', 'Бесплатно']:
            bot.send_message(message.from_user.id, 'Ну и наконец, скажите какой курс вам нужно.')
    elif message.text in ['5 лет', '6 лет', '7 лет', '8 лет', '9 лет', '10 лет', '11 лет', '12 лет', '18 лет', '13 лет', '14 лет', '15 лет', '16 лет', '17 лет', 'Очно', 'Заочно', 'Владимир', 'Суздаль', 'Гороховец', 'Вязники', 'Ковров', 'Александров', 'Январь', 'Февраль', 'Декабрь', 'Март', 'Апрель', 'Май', 'Ноябрь', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'С ОВЗ', 'Без ОВЗ', 'Платно', 'Бесплатно', "Начнём!"]:
            poisk_filtr.append(message.text)
    message_text = message.text
    if message_text not in ['5 лет', '6 лет', '7 лет', '8 лет', '9 лет', '10 лет', '11 лет', '12 лет', '18 лет', '13 лет', '14 лет', '15 лет', '16 лет', '17 лет', 'Очно', 'Заочно', 'Владимир', 'Суздаль', 'Гороховец', 'Вязники', 'Ковров', 'Александров', 'Январь', 'Февраль', 'Декабрь', 'Март', 'Апрель', 'Май', 'Ноябрь', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'С ОВЗ', 'Без ОВЗ', 'Платно', 'Бесплатно', "Начнём!"]:
        slk = bot_poisk(message_text, poisk_filtr, 1)
        print(slk)
        #print(slk)
        text = f'[Вот ваш курс]{slk}'
        bot.send_message(message.chat.id, text, parse_mode='MarkdownV2')
bot.polling()