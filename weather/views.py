import requests
from django.shortcuts import render

def index(request):
    # 1. Start with an empty context (this keeps the screen blank at first)
    context = {}

    if request.method == 'POST':
        city = request.POST.get('city')
        api_key = 'f760f3e666e217eb086d68617411504f'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

        # 2. Only go to the internet if the user actually searched for something
        response = requests.get(url).json()

        if response.get('cod') == 200:
            temp_c = response['main']['temp']
            temp_f = (temp_c * 9/5) + 32 # The conversion formula
            context = {
                'city': response['name'],
                'temp': response['main']['temp'],
                'desc': response['weather'][0]['description'],
                'icon': response['weather'][0]['icon'],
            }
        else:
            context = {
                'city': 'Not Found',
                'temp': '--',
                'desc': 'Please check the city name.',
                'icon': '',
            }

    # 3. Send the 'context' dictionary to the HTML
    return render(request, 'weather/index.html', context)