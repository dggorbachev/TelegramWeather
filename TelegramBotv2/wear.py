import random as rnd

RWeather = ['зонт','дождевик']

CTWeather = ['пуховик','пальто','зимнюю куртку']
CLWeather = ['утеплёнными штанами','утеплёнными брюками','утеплёнными джинсами']
CHWeather = ['перчатки','варежки']

MTWeather = ['куртку','свитер','бомбер','парку','пиджак']
MLWeather = ['плотными джинсами','плотными штанами','плотными брюками','джоггерами']

HTWeather = ['футболку','свитшот','рубашку',]
HLWeather = ['шортами','легкими джинсами','легкими брюками','легкими штанами']

def clothes(temp, typeWeather):
	if temp <= 5 :
		if typeWeather == 'Rain':
			return 'Рекомендуется надеть ' + rnd.choice(CTWeather) + ' с ' + rnd.choice(CLWeather) + ', а так же теплую шапку, шарф и ' + rnd.choice(CHWeather) +  '.\nНе забудьте ' + rnd.choice(RWeather) + '.'
		else:
			return 'Рекомендуется надеть ' + rnd.choice(CTWeather) + ' с ' + rnd.choice(CLWeather) + ', а так же теплую шапку, шарф и ' + rnd.choice(CHWeather) + '.'

	elif temp <= 20:
		if typeWeather == 'Rain':
			return 'Рекомендуется надеть ' + rnd.choice(MTWeather) + ' с ' + rnd.choice(MLWeather) + ', а так же легкую шапку' +  '.\nНе забудьте ' + rnd.choice(RWeather) + '.'
		else:			
			return 'Рекомендуется надеть ' + rnd.choice(MTWeather) + ' с ' + rnd.choice(MLWeather) + ', а так же легкую шапку' + '.'
	else:
		if typeWeather == 'Rain':
			return 'Рекомендуется надеть ' + rnd.choice(HTWeather) + ' с ' + rnd.choice(HLWeather) + '.\nНе забудьте ' + rnd.choice(RWeather) + '.'
		else:
			return 'Рекомендуется надеть ' + rnd.choice(HTWeather) + ' с ' + rnd.choice(HLWeather) + '.'