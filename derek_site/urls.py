from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.http import HttpResponse
from derek_site import views
urlpatterns = patterns('',
    url(r'^weather/', include('get_weather.urls', namespace='weather')),
    url(r'^(dr|riemer|personal|derek)/', include('personal.urls', namespace='personal')),
    url(r'^admin/', include(admin.site.urls)),
)
print views
handler404 = 'derek_site.views.error404'