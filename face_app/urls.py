from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views
urlpatterns = [
    path('', views.intro,name='front'),
    path('doctor/', include('django.contrib.auth.urls')),
    path('aadharlogin/', views.aadharlogin, name='aadharlog'),
    url(r'^details/(?P<id>\d+)/files/$', views.files, name='files'),
    url(r'^details/(?P<id>\d+)/files/new/$', views.newfiles, name='newfiles'),
    path('pharma/', views.pharmacy, name='pharmacy'),
    path('pharma/otpa/', views.otpa, name='otpa'),
    path('pharma/otpa/<int:id>/', views.otparecord, name='otpa_record'),
    path('patient/', views.patient, name='patient'),

]
