from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.http import HttpResponse
urlpatterns = patterns('',
    url(r'^weather/', include('get_weather.urls', namespace='weather')),
    url(r'^(dr|riemer|personal|derek)/', include('personal.urls', namespace='personal')),
    url(r'^admin/', include(admin.site.urls)),
)
#handler404 = 'get_weather.views.error404'