import telebot
import config

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['help'])
def send_welcome(message):
	bot.send_message(message.chat.id,
		"""Не расстраивайтесь.\n
		Давайте вместе составим команду, чтобы я смог вам все посчитать😋\n
		Первое слово - количество листов (цифрой).
		<i>Например:</i> 6\n
		Второе слово - размер конверта (большой или маленький).
		<i>Например:</i> большой\n
		Третье слово - тип письма (простое или заказное).
		<i>Например</i>: простое\n
		Все вместе будет: <b>6 большой простое</b>\n
		Если у вас заказное письмо с уведомлением, добавьте букву "у" в ваше сообщение\n
		Например: <b>8 большой заказное у</b>\n
		У нас получится. Дерзайте!""".format(message.from_user, bot.get_me()),
	parse_mode='html')

@bot.message_handler(commands=['start'])
def send_welcome(message):
	sti = open('hello.webp', 'rb')
	bot.send_sticker(message.chat.id, sti)
	bot.send_message(message.chat.id, 
		"""Привет, {0.first_name}!

		Я - <b>{1.first_name}</b>. Я могу написать вам сколько весит и стоит ваше письмо😋

		Пришлите мне сообщение в формате:
		кол-во листов большой/маленький(конверт) заказное/простое

		<i>Например:</i> <b>3 маленький заказное</b>

		Если у вас заказное письмо с уведомлением, 
		добавьте букву "у" в ваше сообщение\n
		<i>Например</i>: <b>8 большой заказное у</b>

		Я еще маленький, поэтому не ругайстесь, если я что-то не пойму🥺
		Лучше напишите свои пожелания моему создателю @elisei_34""".format(message.from_user, bot.get_me()),
		parse_mode='html')

@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
	bot.send_message(message.chat.id, count_weigth(message.text).format(message.from_user, bot.get_me()),
	parse_mode='html')

def count_weigth(message):
	try:
		notification_weight = 0
		k = False
		lst = message.lower().split()
		paper_weight = int(lst[0])*config.PAPER	

		if 'большой' in lst or 'большое' in lst:
			envelope_weight = config.BIG_ENVELOPE
		elif 'маленький' in lst or 'маленькое' in lst:
			envelope_weight = config.SMALL_ENVELOPE

		if 'у' in lst:
			notification_weight = float(config.NOTIFICATION)
			k = True

		all_weight = float(paper_weight) + float(envelope_weight) + notification_weight

		if 'заказное' in lst or 'заказной' in lst:
			link = "\nНе забуддьте зарегистрировать ваше заказное письмо в <a href='https://forms.gle/6ZHmR3ZAme5PnBoAA'>реестре</a>"
			if k:
				koef = config.NOTIFICATION_K
			else:
				if all_weight < 100:
					koef = config.LETTER_K
				else:
					koef = config.PARSEL_K

		elif 'простое' in lst or 'простой' in lst:
			link =''
			koef = 0

		if all_weight <=20:
			all_sum = int(config.TARIF_20GR + koef)
		elif 20 < all_weight <= 40:
			all_sum = int(config.TARIF_40GR + koef)
		elif 40 < all_weight <= 60:
			all_sum = int(config.TARIF_60GR + koef)
		elif 60 < all_weight <= 80:
			all_sum = int(config.TARIF_80GR + koef)
		elif 80 < all_weight <= 100:
			all_sum = int(config.TARIF_100GR + koef)
		elif 100 < all_weight <= 120:
			all_sum = int(config.TARIF_120GR + koef)
		elif 120 < all_weight <= 140:
			all_sum = int(config.TARIF_140GR + koef)
		elif 140 < all_weight <= 160:
			all_sum = int(config.TARIF_160GR + koef)
		elif 160 < all_weight <= 180:
			all_sum = int(config.TARIF_180GR + koef)
		elif 180 < all_weight <= 200:
			all_sum = int(config.TARIF_200GR + koef)
		elif 200 < all_weight <= 220:
			all_sum = int(config.TARIF_220GR + koef)
		elif 220 < all_weight <= 240:
			all_sum = int(config.TARIF_240GR + koef)
		elif 240 < all_weight <= 260:
			all_sum = int(config.TARIF_260GR + koef)
		elif 260 < all_weight <= 280:
			all_sum = int(config.TARIF_280GR + koef)
		elif 280 < all_weight <= 300:
			all_sum = int(config.TARIF_300GR + koef)
		elif 300 < all_weight <= 320:
			all_sum = int(config.TARIF_320GR + koef)
		elif 320 < all_weight <= 340:
			all_sum = int(config.TARIF_340GR + koef)
		elif 340 < all_weight <= 360:
			all_sum = int(config.TARIF_360GR + koef)
		elif 360 < all_weight <= 380:
			all_sum = int(config.TARIF_380GR + koef)
		elif 380 < all_weight <= 400:
			all_sum = int(config.TARIF_400GR + koef)
		elif 400 < all_weight <= 420:
			all_sum = int(config.TARIF_420GR + koef)
		elif 420 < all_weight <= 440:
			all_sum = int(config.TARIF_440GR + koef)
		elif 440 < all_weight <= 460:
			all_sum = int(config.TARIF_460GR + koef)
		elif 460 < all_weight <= 480:
			all_sum = int(config.TARIF_480GR + koef)
		elif 480 < all_weight <= 500:
			all_sum = int(config.TARIF_500GR + koef)
		else:
			return('😱 Ваш конверт слишком тяжелый. Давайте уберем пару листочков 😏')

		return('Вес письма: ' + str(all_weight) + ' гр\nНа сумму: ' + str(all_sum) + ' р.' + str(link))

	except:
		return('Я вас не понял 😕. Воспользуйтесь командой /help если совсем запутались.')

bot.polling(none_stop=True)