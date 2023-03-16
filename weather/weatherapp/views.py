import json
from django import http
from django.shortcuts import render
import urllib.request

# Create your views here.

def index(request):
    if request.method=='POST':
        city=request.POST['city']
        res=urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=f66af6f14f798abebe6c4f0dd1d8d2d4').read()
        json_data=json.loads(res)
        data={
            'country':str(json_data["sys"]["country"]),
            'coordinate':str(json_data["coord"]["lon"])+" "+str(json_data["coord"]["lat"]),
            'temp':str(json_data["main"]["temp"])+ "k",
            'humidity':str(json_data["main"]["humidity"]),
        }
    else:
        data={}
    return render(request,'index.html',data)