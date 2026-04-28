import requests # A library that lets Python "visit" websites (APIs)
from django.shortcuts import render # Helps us "draw" the HTML on the screen

# Create your views here.
def index(request):
    # 1. Grab the city name from the search bar (the URL)
    # If the user hasn't typed anything yet, default to 'London'
    city = request.GET.get('city', 'London')

    # 2. Setup our API info (We'll need a real key soon!)
    api_key = 'f760f3e666e217eb086d68617411504f'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

    # 3. Go get the data from the internet
    response = requests.get(url).json() # Convert the data to a Python dictionary

    # Logic Check: Did the API find the city? (Status code 200 means "OK")
    if response.get('cod') == 200:
        context = {
            'city': response['name'],
            'temp': response['main']['temp'],
            'desc': response['weather'][0]['description'],
            'icon': response['weather'][0]['icon'], # A code for the weather icon (e.g. '01d')
        }
    else:
        # If the city isn't found, we send back an error message
        context = {
            'city': 'Not Found',
            'temp': '--',
            'desc': 'Please check the city name.',
            'icon': '',
        }
    # 5. Send that info to the HTML file
    return render(request, 'weather/index.html', context)