"""This file Copyright (C) Derek Riemer, 2015
	This file is part of my personal website.

	my personal website is free software: you can redistribute it and/or modify
	it under the terms of the GNU Affero General Public License as published by
	the Free Software Foundation, either version 3 of the License, or
	(at your option) any later version.

	The code of my personal website is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with my personal website.  If not, see <http://www.gnu.org/licenses/>."""
from django.shortcuts import get_object_or_404, render
import datetime
import forecastio
from django.http import Http404
import os

API_KEY= open(os.path.join(os.path.dirname(__file__), 'apikey').replace('\\','/')).read(100)            
#helper functions.

def makeIds():
    a=1
    while True:
        b=(yield a) #allow for it to be changed.
        if b is not None:
            a=b-1 #generate b again for whatever reason.
        a+=1

def pre(id):
    return u"<span id=\"{}\"><script>var d=new Date(".format(id)

def post(id):
    return u"); document.getElementById(\""+id+"\").innerHTML=friendlyHourNames(d.getHours());</script></span>"

def getJavascriptTagForSeconds(dt, id):
    """Converts a datetime into a javascript blob that coerces into the local time reading standard when run.
    """
    return pre(id)+str(int((dt - datetime.datetime(1970, 1, 1)).total_seconds())*1000)+post(id)

def getJavascriptTag(dt, id):
    """Converts a time into a javascript blob that coerces into the local time reading standard when run.
    """
    return pre(id)+str(dt*1000)+post(id)

class Forecast:
    cashe=None
    #helper functions.

    def isCasheValid(self):
        if Forecast.cashe is not None:
            td=datetime.datetime.now()-Forecast.cashe.time
            if td.total_seconds() < 300:
                return True
            return False
        else:
            return False

    def loadForecast(self, request):
        if self.isCasheValid():
            return Forecast.cashe
        else:
            #print "Expunging weather cashe"
            try:
                lat=request.POST['lat']
                lng = request.POST['lng']
            except KeyError:
                raise Http404("bad request")
            forecast = forecastio.load_forecast(API_KEY, lat, lng)
            
            #Forecast.cashe=forecast
            #Forecast.cashe.time=datetime.datetime.now()
        return forecast



    def windy(self, speed):
        if speed <= 10:
            return "calm"
        elif speed > 10 and speed <= 15:
            return "breezy"
        elif speed > 15 and speed <= 20:
            return "quite breezy"
        elif speed > 20 and speed <= 30:
            return "windy"
        elif speed > 30 and speed <= 40:
            return "quite windy"
        elif speed > 40 and speed <= 75:
            return "extremely windy"
        else:
            return "a hurricane forced wind."

#views.

def getContext():
    return {
        "MENU_FILE" : "get_weather/menu.htm"
    }



def forecast(request):
    if request.method=="POST":
        try:
            page     = request.POST["page"]
        except KeyError:
            return Http404("Not a valid page.")
        if page=="home":
            return index(request, True)
        elif page=="hourly":
            return hourly(request, True)
        elif page=="daily":
            return daily(request, True)
        else:
            return Http404("error, bad post request!")

def hourly(request, data=False):
    context=getContext()
    if data==True:
        idNum=makeIds()
        weather=Forecast()
        forecast=weather.loadForecast(request)
        hourly=forecast.hourly()
        hourData = []
        for i in hourly.data[:24]:
            id="\"hourly_"+str(next(idNum))+'"'
            hourData.append({
                "id" : id,
                "tag": "<span id="+id+"></span>",
                "script": str(i.time*1000),
                "temp": i.temperature,
                "precip": (i.precipProbability*100)
            })
        context['forecasted'] = hourData
        return render(request, 'get_weather/hourly_forecast.htpartial', context)
    else:
        return render(request, 'get_weather/hourly.htm', context)


def index(request, data=False): #data will make sure that this gets location or checks for the cashe first.
    #print(data)
    context=getContext()
    if data==True:
        curLst = []
        weather=Forecast()
        forecast = weather.loadForecast(request)
        current=forecast.currently()
        curLst .append(u"It is currently {0} and {1}&#xb0; F".format(current.summary, int(current.temperature)))
        day=forecast.daily()
        today=day.data[0]
        curLst.append(u"Today: {0}".format(today.summary))
        if today.precipProbability != 0:
            curLst.append(u"there is a {0:.0%} chance of precipitation.".format(today.precipProbability))
        else:
            curLst.append(u"No precipitation expected today.")
        
        highTime= getJavascriptTag(today.temperatureMaxTime, "high_1")
        curLst.append(u"daily high {0}&#xb0; F at {1}".format(today.temperatureMax, highTime))
        lowTime=getJavascriptTag(today.temperatureMinTime, "low_1")
        curLst.append(u"daily low {0}&#xb0; at {1}".format(today.temperatureMin, lowTime))
        curLst.append(u"It is {0}, the wind speed is {1} mph".format(weather.windy(today.windSpeed), today.windSpeed))
        context['curLst'] = curLst
        return render(request, 'get_weather/current_forecast.htpartial', context)
    else:
        return render(request, 'get_weather/index.htm', context)

def daily(request, data=False):
    context=getContext()
    idNum=makeIds()
    if data==True:
        weather = Forecast()
        forecast=weather.loadForecast(request)
        daily = forecast.daily()
        W_DAYS = ['Monday', 'Tuesday', 'Wednesday','Thursday', 'Friday', 'Saturday', 'Sunday']
        forecasted=[]
        for i in daily.data:
            formatter=[]
            try:
                formatter.append(W_DAYS[datetime.datetime.fromtimestamp(i.time).weekday()])
                formatter.append(i.summary)
                a=str(next(idNum))
                temperatureMaxTime = getJavascriptTag(i.temperatureMaxTime, "maxt_"+a)
                temperatureMinTime = getJavascriptTag(i.temperatureMinTime, "mint_"+str(a))
                formatter.append(u"high temperature: {0}&#xb0;F at {1}".format(i.temperatureMax, temperatureMaxTime))
                formatter.append(u"low temperature: {0}&#xb0;F at {1}".format(i.temperatureMin, temperatureMinTime))
                precip=""
                if i.precipProbability > 0:
                    precip+="chance of "+i.precipType
                    precip+="{:.0%}".format(i.precipProbability)
                else:
                    precip+='No precipitation is expected '
                formatter.append(precip)
                formatter.append("It will be {0}: with a wind speed of approximately {1} mph.".format(weather.windy(i.windSpeed), i.windSpeed))
                forecasted.append(formatter)
            except  NameError as e:
                forecasted.append("error retreiving current days wether.")
        context['forecasted']= forecasted
        return render(request, 'get_weather/daily_forecast.htpartial', context)
    else:
        return render(request, 'get_weather/daily.htm', context)

