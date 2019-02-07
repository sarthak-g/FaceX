from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^details/(?P<id>\d+)/$', views.details, name='details'),
    url(r'^pdetails/(?P<id>\d+)/$', views.pdetails, name='pdetails'),
    url(r'^details/(?P<id>\d+)/files/$', views.files, name='files'),
    url(r'^details/(?P<id>\d+)/files/newfiles/$', views.newfiles, name='newfiles'),
]
