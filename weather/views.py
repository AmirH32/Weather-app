from django.shortcuts import render
import json
import urllib.request

# Create your views here.

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=c0e3226939790ef810b46ffbd789e9e7').read()
        json_data = json.loads(res)
        data = {
            "temp": str(int(json_data['main']['temp'])-273)+'°C',
            "temp_Feels": str(int(json_data['main']['feels_like'])-273)+'°C',
            "pressure": str(json_data['main']['pressure']),
            "humidity": str(json_data['main']['humidity']),
            "weather":str(json_data['weather'][0]['main']),
            "weather_Description":str(json_data['weather'][0]['description']),
            "wind_Speed":str(json_data['wind']['speed'])
        }

    else:
        city = ''
        data = {}
    return render(request, 'index.html',{'city':city,'data':data})

