# WeatherBot
This bot gets weather everyday and sends a text message to user with information about the days forecast. The current tempurature and conditions will be sent along with the temperature for 10AM, 1PM, 4PM, 7PM, and 10PM. The program also determines if there is a large enough chance for rain that day for the user to bring their raincoat or umbrella.

## Uses
This program's main use is to keep the user up to date everyday by sending the weather with the forecast for the day to their phone to see when they wake up. This program allows the user to plan their day based on the temperature and weather seen easily as a notification right when they turn their phone on. 

## Prerequisites
This program runs on python 3.7.4 and requires the twilio packages to be installed.

```
pip install twilio
```

## Set Up
All areas that require personal information in the program will be denoted with *****

Follow these steps to set up the program:
  
* Enter your twilio client account id and auth token. Visit [Twilio](https://www.twilio.com) to make a free account.
* Register and get an openweathermap api key [here](https://openweathermap.org/api)
* Connect the openweathermap current and 5 day forecast with your current zip code and api key
* Add the phone number you wish to recieve notifications to and your twilio account number to send messages from.

## Deployment
This program was built with the idea of being put on a Raspberry Pi and to be ran every few minutes through a cron job. 
However it can run on any system and scheduled by a cron job or its equivalent such as a scheduled task. 

I built this program notify me at 6:30AM every morning and as such they list logic is all set up to refelct that and the forecast for the rest of the day. To change the times you will have to change that logic.

## Author
joeromsa
