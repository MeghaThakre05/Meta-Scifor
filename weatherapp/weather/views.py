import requests
from django.shortcuts import render
from django.http import HttpResponse


def get_weather(city):
    api_key = 'c41e6802ae298ecd4ec59d6eb1b2f4b1'  # Replace with your OpenWeatherMap API key
    base_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

    response = requests.get(base_url)
    return response.json()


def weather_view(request):
    city = request.GET.get('city', 'Hyderabad')  # Default to Hyderabad if no city is provided
    weather_data = get_weather(city)

    if weather_data.get('cod') != 200:
        return HttpResponse("City not found!", status=404)

    # Extract relevant data from the API response
    city_name = weather_data['name']
    weather_description = weather_data['weather'][0]['description']
    temperature = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']
    pressure = weather_data['main']['pressure']

    context = {
        'city_name': city_name,
        'weather_description': weather_description,
        'temperature': temperature,
        'humidity': humidity,
        'pressure': pressure
    }

    return render(request, 'weather/weather.html', context)

