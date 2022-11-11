# -*- coding: utf-8 -*-

import tkinter as tk
import requests


def getWeather():
    clear()
    api = 'a19f0ddc1574fd7839c2ef5b50924d4e'
    
    location = city_value.get()
    location_2 = city_value_2.get()
    
    part = None
  
    weather_url = f'https://api.openweathermap.org/data/2.5/weather?q={location}&appid=b0ee83e54a7746062916a80a9e32193a&units=metric'
    weather_url_2 = f'https://api.openweathermap.org/data/2.5/weather?q={location_2}&appid=b0ee83e54a7746062916a80a9e32193a&units=metric'
  
    response = requests.get(weather_url)
    response_2 = requests.get(weather_url_2)
 
    weather_info = response.json()
    weather_info_2 = response_2.json()    

    temp = int(weather_info['main']['temp']) 
    feels_like_temp = int(weather_info['main']['feels_like'])
    pressure = weather_info['main']['pressure']
    humidity = weather_info['main']['humidity']
    wind_speed = weather_info['wind']['speed'] * 3.6
    sunrise = weather_info['sys']['sunrise']
    sunset = weather_info['sys']['sunset']
    timezone = weather_info['timezone']
    cloudy = weather_info['clouds']['all']
    description = weather_info['weather'][0]['description']
     
    
    weather = f"\nWeather of: {location}\nTemperature (Celsius): {temp}°\nFeels like in (Celsius): {feels_like_temp}°\nPressure: {pressure} hPa\nHumidity: {humidity}%\nCloud: {cloudy}%\nInfo: {description}"

    test_field.insert(tk.INSERT,weather)

    temp = int(weather_info_2['main']['temp']) 
    feels_like_temp = int(weather_info_2['main']['feels_like'])
    pressure = weather_info_2['main']['pressure']
    humidity = weather_info_2['main']['humidity']
    wind_speed = weather_info_2['wind']['speed'] * 3.6
    sunrise = weather_info_2['sys']['sunrise']
    sunset = weather_info_2['sys']['sunset']
    timezone = weather_info_2['timezone']
    cloudy = weather_info_2['clouds']['all']
    description = weather_info_2['weather'][0]['description']
     
    # sunrise_time = time_format_for_location(sunrise + timezone)
    # sunset_time = time_format_for_location(sunset + timezone)
    
    weather2 = f"\nWeather of: {location_2}\nTemperature (Celsius): {temp}°\nFeels like in (Celsius): {feels_like_temp}°\nPressure: {pressure} hPa\nHumidity: {humidity}%\nCloud: {cloudy}%\nInfo: {description}"

    test_field2.insert(tk.INSERT,weather2)


def clear():
    test_field.delete('1.0',tk.END)
    test_field2.delete('1.0',tk.END)

root = tk.Tk()
root.title('Weather App For Traveler')
root.geometry('400x550')
# background_image=tk.PhotoImage(file="C:/Users/Mcggvc/Desktop/IMG_0092.JPG")
# background_label = tk.Label(root, image=background_image)
# background_label.place(x=0, y=0, relwidth=1, relheight=1)


first_label = tk.Label(root, text='Location', fg='Blue',bg='Yellow',font=('Times',16))
first_label.pack(pady=30)

city_value = tk.StringVar()
city_value_2 = tk.StringVar()
location_to_search = tk.Entry(root, textvariable=city_value, width=24,font=('Times',16))
location_to_search_2 = tk.Entry(root, textvariable=city_value_2, width=24,font=('Times',16))
city_value.set('Departure')
city_value_2.set('Destination')
location_to_search.pack()
location_to_search_2.pack()

search_button = tk.Button(root, command = getWeather, text='Search', font=('Times', 16), bg='Grey')
search_button.pack(pady=10)

clear_button = tk.Button(root, command = clear, text='Clear', font=('Times', 16), bg='Grey')
clear_button.pack(pady=10, side = tk.RIGHT)

second_label = tk.Label(root, text='Weather Information', fg='Blue',bg='Yellow',font=('Times',16))
second_label.pack(pady=10)

test_field = tk.Text(root, width=46, height=10)
test_field2 = tk.Text(root, width=46, height=10)
test_field.pack()
test_field2.pack()


root.mainloop()
