from django.conf.urls import patterns, url

from personal import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='home'),
    url(r'^bio$', views.bio, name='bio'),
)
