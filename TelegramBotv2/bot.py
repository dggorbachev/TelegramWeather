import telebot
import config
import cityWeather as cw
import wear

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start','help','reroll'])
def req(mes):
	if mes.text == '/help':
		bot.send_message(mes.chat.id, 'Для получения информации о погоде в городе, введите его и отправьте мне.')
	elif mes.text == '/start':
		bot.send_message(mes.chat.id, 'Начнем! Для справки выберите команду /help.')
	elif mes.text == '/reroll':
		try:
			if(message1 == ''):
				bot.send_message(message1.chat.id, 'Город еще не был введен. Для справки выберите команду /help.')
			else:
				cw.cityWeather(message1)
				res = wear.clothes(int(cw.temp), cw.w.status)
				bot.send_message(message1.chat.id, str(cw.result) + '\n' + str(res))
		except:
			bot.send_message(message1.chat.id, 'Город еще не был введен. Для справки выберите команду /help.')
	else:
		bot.send_message(mes.chat.id, 'Введена несуществующая команда. Для справки выберите команду \n /help.')

message1 = ''
@bot.message_handler(content_types=['text'])
def main(message):
	try:
		global message1
		message1 = message
		cw.cityWeather(message)
		res = wear.clothes(int(cw.temp), cw.w.status)
		bot.send_message(message.chat.id, str(cw.result) + '\n' + str(res))
	except:
		bot.send_message(message.chat.id, 'Введен несуществующий город.')

bot.polling(none_stop=True)