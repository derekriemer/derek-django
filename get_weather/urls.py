from django.conf.urls import patterns, url

from get_weather import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='home'),
    url(r'^daily$', views.daily, name='daily'),
    url(r'^forecast$', views.forecast, name='forecast'),
    url(r'^hourly$', views.hourly, name='hourly'),
    
)
