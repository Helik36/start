#  https://habr.com/ru/post/448310/
#  https://github.com/eternnoir/pyTelegramBotAPI#getting-started
import telebot
import sys, os, datetime

def save_info(message):
	current_time = datetime.datetime.now()
	result = f'{current_time} - {message}'
	print(result)
	with open('real_logs.txt', 'a', encoding='utf-8') as f:
		f.write(result + '\n')

bot = telebot.TeleBot('1080238380:AAFdjtTIzSoRcFDy3ky6pMLbHrpnlaNLqcQ')


keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True) # первый Тру, чтобы кнопки были небольшие, второй, чтобы скрывалась после нажатия
keyboard1.row('Привет', 'Пока')
save_info('старт')
@bot.message_handler(commands=['start'])

def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])

def send_text(message):
	save_info(message.chat.id) # показывает айди человека, который написал
	save_info(message.text) # показывает сообщение
	if message.text.lower() == 'привет':
		bot.send_message(message.chat.id, 'Привет!')
	elif message.text.lower() == 'пока':
		bot.send_message(message.chat.id, 'Ну пока :c')
	elif message.text.lower() == 'я тебя люблю':
		bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAM4Xmt4u2qWXh6zfvwkmY-ePqRNZQcAAhkAA8A2TxPQQ4D2IFcUSxgE')

@bot.message_handler(content_types=['sticker'])

def ssend_sticker(message):
	print(message)

bot.polling()
