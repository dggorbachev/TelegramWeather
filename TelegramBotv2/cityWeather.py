from pyowm import OWM

owm = OWM('3f5d03c135a383020128e6e80209917f')
result = ''
w = ''
temp = ''
def cityWeather(message):
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(message.text)
    global w
    w = observation.weather
    global temp
    temp = w.temperature('celsius')['temp']
    global result
    result = 'В городе ' + str(message.text) + ' сейчас температура: ' + str(temp) + ' по Цельсию.'