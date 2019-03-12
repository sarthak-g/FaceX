from django.urls import path
from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    path('pharma', views.pharmacy, name='pharmacy'),
    path('pharma/otpa', views.otpa, name='otpa'),
    path('pharma/otpa/<int:id>/', views.otparecord, name='otpa_record'),

    url(r'^details/(?P<id>\d+)/$', views.details, name='details'),
    url(r'^pdetails/(?P<id>\d+)/$', views.pdetails, name='pdetails'),
    url(r'^pdetails/(?P<id>\d+)/pfiles/$', views.pfiles, name='particular_prescription'),

    url(r'^details/(?P<id>\d+)/files/$', views.files, name='files'),
    url(r'^details/(?P<id>\d+)/files/newfiles/$', views.newfiles, name='newfiles'),
]
