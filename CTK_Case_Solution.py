import requests
import math

try:
    city_name = str(input("Enter a city name or a country name: ")).capitalize()
    api_key = ""

    def weather_report(api, city):
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}"
        response = requests.get(url).json()
        temp = response['main']['temp']
        temp = math.floor(temp - 273.15)  # Conversion to celsius
        feels_like = response['main']['feels_like']
        feels_like = math.floor(feels_like-273.15)
        if feels_like != temp:
            print(f"\nThe temperature in {city_name} is {temp} degree celsius,\nbut it feels like {feels_like} degree celsius!")
        else:
            print(f"\nThe temperature in {city_name} is {temp} degree celsius,\nand it also feels like {feels_like} degree celsius!")

    weather_report(api_key, city_name)

except KeyError:
    print("\nInvalid city or country name")

finally:
    print("\nThank you for running this program!")
