from django.shortcuts import get_object_or_404, render
import datetime
import forecastio

cashe=None
#helper functions.

def isCasheValid():
    global cashe
    if cashe is not None:
        td=datetime.datetime.now()-cashe.time
        if td.total_seconds() < 300:
            return True
        return False
    else:
        return False

def loadForecast():
    global cashe
    if isCasheValid():
        return cashe
    else:
        print "Expunging weather cashe"
        api_key = "af5e4568466e3d31b3dbb558d5dc8758"
        lat=40.014986
        lng=-105.270546
        forecast = forecastio.load_forecast(api_key, lat, lng)
        cashe=forecast
        cashe.time=datetime.datetime.now()
    return cashe

def windy(speed):
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
    forecast=loadForecast()
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
    """
    current=forecast.currently()
    hourly=forecast.hourly()
    context = {
        'forecast' : forecast,
        'current' : current,
        'hourly': hourly,
    }
    """
    context={
    
    }
    return render(request, 'get_weather/index.htm', context)

def daily(request):
    forecast=loadForecast()
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
            formatter['wind'] = windy(i.windSpeed)+" Wind speed: "+str(int(i.windSpeed))+" mph "
            forecasted.append("{weekday}: {summary} {wind}High: {temperaturemax} degrees at {temperaturemaxtime}. Low: {temperaturemin} Degrees  at {temperaturemintime}. {preciptype}{precipprobability}".format(**formatter))
        except  NameError as e:
            forecasted.append(e.message)


    context={
        'forecasted': forecasted,
    }
    return render(request, 'get_weather/daily.htm', context)