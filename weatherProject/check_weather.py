import requests
import json
from twilio.rest import Client

#Converts kelvin to farenheight.
def k_to_f(temp):
    temp = (temp * 1.8) - 459.67
    return temp

#Takes the numerical representation of how strong the wind is and returns it as a string. 
def wind_type(wind):
    if wind <= 1:
        return 'calm'
    elif wind > 1 and wind <= 7:
        return 'light breeze'
    elif wind > 7 and wind <= 18:
        return 'moderate breeze'
    elif wind > 18 and wind <= 30:
        return 'strong wind'
    else:
        return 'extremely strong wind'

#Calculates average wind speed between 10am and 10pm. 
def ave_wind_num(wind_list):
    total = 0
    for item in wind_list[1:5]:
        total = total + item
    
    return round(total / 5)

#Checks if it will be raining between 10AM - 10PM.
def need_rain_jacket():
    if weather_desc[1] == 'light rain' or weather_desc[2] == 'light rain' or weather_desc[3] == 'light rain' or weather_desc[4] == 'light rain' or weather_desc[5] == 'light rain':
        return ''
    elif weather_main[1] == 'Rain' or weather_main[2] == 'Rain' or weather_main[3] == 'Rain' or weather_main[4] == 'Rain' or weather_main[5] == 'Rain':
        return ', bring rain jacket'
    else:
        return ''

#Api calls and auth for messages.
client = Client("*****","*****")
response = requests.get('https://api.openweathermap.org/data/2.5/forecast?zip=68059,us&appid=935e4c109dfacaa7bc30b5876146626a')
current = requests.get('https://api.openweathermap.org/data/2.5/weather?zip=68059,us&appid=935e4c109dfacaa7bc30b5876146626a')
data = response.json()
current_data = current.json()

#Lists and variables to hold data.
current_temp = k_to_f(current_data['main']['temp'])
current_weather_main = current_data['weather'][0]['main']
current_weather_description = current_data['weather'][0]['description']
current_wind = current_data['wind']['speed']
temp = []
time = []
weather_main = []
weather_desc = []
wind = []

#Strings to build the message with.
intro = '\nGood Morning Joe\nHere is your Forecast for the Day\n\n'
now = 'Current Temp: '
degrees = ' degrees F\n'
weather = 'Weather for the Day: '
tenam = '\n\n10 AM: '
one = '\n1 PM: '
four = '\n4 PM: '
seven = '\n7 PM: '
tenpm = '\n10 PM: '
close = '\n\nHave a Great Day'

#Loops to put weather data in lists.
for obj in data['list']:
    temp.append(obj['main']['temp'])
    time.append(obj['dt_txt'])
    wind.append(obj['wind']['speed'])

for obj in data['list']:
    for x in obj['weather']:
        weather_main.append(x['main'])
        weather_desc.append(x['description'])

#Finding average wind for the day.
wind_ave = ave_wind_num(wind)
wind_text = wind_type(wind_ave)

msg = intro + now + str(round(current_temp)) + degrees + weather + current_weather_description + ', ' + wind_text + need_rain_jacket() + tenam + str(round(k_to_f(temp[1]))) + ' F' + one + str(round(k_to_f(temp[2]))) + ' F' + four + str(round(k_to_f(temp[3]))) + ' F' + seven + str(round(k_to_f(temp[4]))) + ' F' + tenpm + str(round(k_to_f(temp[5]))) + ' F' + close

client.messages.create(to="+*****", from_="+*****", body=msg)
