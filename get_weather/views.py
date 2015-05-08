from django.shortcuts import get_object_or_404, render
import datetime
import forecastio

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

    def loadForecast(self):
        if self.isCasheValid():
            return Forecast.cashe
        else:
            print "Expunging weather cashe"
            api_key = "af5e4568466e3d31b3dbb558d5dc8758"
            lat=40.014986
            lng=-105.270546
            forecast = forecastio.load_forecast(api_key, lat, lng)
            Forecast.cashe=forecast
            Forecast.cashe.time=datetime.datetime.now()
        return Forecast.cashe

    def windy(self, speed):
        if speed <= 10:
            return "calm"
        elif speed > 10 and speed <= 15:
            return "breezey"
        elif speed > 15 and speed <= 20:
            return "quite breezey"
        elif speed > 20 and speed <= 30:
            return "windy"
        elif speed > 30 and speed <= 40:
            return "quite windy"
        elif speed > 40 and speed <= 75:
            return "extremely windy"
        else:
            return "a hurricane forced wind."
            pass

#views.
def error404(request):
    return render(request, '404.htm', {})

def hourly(request):
    weather=Forecast()
    forecast=weather.loadForecast()
    hourly=forecast.hourly()
    hourData=[(i.time, i.temperature, (i.precipProbability*100)) for i in hourly.data]
    i=hourData[0][0].hour
    lastIndex=1
    while lastIndex<len(hourData):
        if hourData[lastIndex][0].hour == i: #24 hours has passed.
            break
        lastIndex+=1
    context={
        'forecasted' : hourData[:lastIndex+1]
    }
    return render(request, 'get_weather/hourly.htm', context)


def index(request):
    curLst = []
    weather=Forecast()
    forecast = weather.loadForecast()
    current=forecast.currently()
    curLst .append("It is currently {0} and {1} degrees f".format(current.summary, int(current.temperature)))
    day=forecast.daily()
    today=day.data[0]
    curLst.append("Today: {0}".format(today.summary))
    curLst.append("there is a {0:.0%} chance of precipitation.".format(today.precipProbability))
    highTime= datetime.datetime.fromtimestamp(today.temperatureMaxTime)
    curLst.append("daily high {0} at {1}".format(today.temperatureMax, highTime.strftime("%I:%M %p")))
    lowTime=datetime.datetime.fromtimestamp(today.temperatureMinTime)
    curLst.append("daily low {0} at {1}".format(today.temperatureMin, lowTime.strftime("%I:%M %p")))
    curLst.append("It is {0}, the wind speed is {1} mph".format(weather.windy(today.windSpeed), today.windSpeed))
    
    context = {
        'curLst' : curLst,
    }


    return render(request, 'get_weather/index.htm', context)

def daily(request):
    weather = Forecast()
    forecast=weather.loadForecast()
    daily = forecast.daily()
    W_DAYS = ['Monday', 'Tuesday', 'Wednesday','Thursday', 'Friday', 'Saturday', 'Sunday']
    forecasted=[]
    for i in daily.data:
        formatter={}
        try:
            formatter['weekday'] = W_DAYS[i.time.weekday()]
            tmxt = datetime.datetime.fromtimestamp(i.temperatureMaxTime)
            tmnt = datetime.datetime.fromtimestamp(i.temperatureMinTime)
            temperatureMaxTime = "{:02}:{:02}".format(tmxt.hour, tmxt.minute)
            temperatureMinTime = "{:02}:{:02}".format(tmnt.hour, tmnt.minute)
            formatter['temperaturemax']=i.temperatureMax
            formatter['temperaturemaxtime'] = temperatureMaxTime
            formatter['temperaturemin'] = i.temperatureMin
            formatter['temperaturemintime'] = temperatureMinTime
            if i.precipProbability > 0:
                formatter['preciptype']= "chance of "+i.precipType
                formatter['precipprobability'] = "{:.0%}".format(i.precipProbability)
            else:
                formatter['preciptype'] = 'No precipitation is expected '
                formatter['precipprobability'] = ""
            formatter['summary'] = i.summary
            formatter['wind'] = weather.windy(i.windSpeed)+" Wind speed: "+str(int(i.windSpeed))+" mph "
            forecasted.append("{weekday}: {summary} {wind}High: {temperaturemax} degrees at {temperaturemaxtime}. Low: {temperaturemin} Degrees  at {temperaturemintime}. {preciptype}{precipprobability}".format(**formatter))
        except  NameError as e:
            forecasted.append(e.message)


    context={
        'forecasted': forecasted,
    }
    return render(request, 'get_weather/daily.htm', context)