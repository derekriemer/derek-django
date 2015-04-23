from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.http import HttpResponse
urlpatterns = patterns('',
    url(r'^weather/', include('get_weather.urls', namespace='weather')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^flocking$', lambda request: HttpResponse(open("./flocking/flocking-all.js", "rb").read(), content_type="text/plain")), #return an http response with the flocking file.
)
#handler404 = 'get_weather.views.error404'