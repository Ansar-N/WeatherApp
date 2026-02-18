from django.shortcuts import render
import requests

def home(request):
    city = "Chennai"   

    if request.method == "POST":
        city = request.POST.get("city")

    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": "ENTER USER APIKEY",  
        "units": "metric"
    }

    response = requests.get(url, params=params)
    data = response.json()

    weather_data = {}

    if response.status_code == 200:
        weather_data = {
            "city": city,
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "icon": data["weather"][0]["icon"]
        }
    else:
        weather_data = {
            "error": data.get("message", "Something went wrong")
        }

    return render(request, "index.html", {"weather": weather_data})
