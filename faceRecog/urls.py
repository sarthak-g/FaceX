"""faceRecog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from faceRecog import views as app_views
from django.urls import path

urlpatterns = [
    url(r'^$', app_views.intro,name='front'),
    url(r'^home/$', app_views.index,name='home'),
    url(r'^home/patient/$', app_views.indexp,name='patient_home'),
    url(r'^home/', include('django.contrib.auth.urls')),

    url(r'^error_image$', app_views.errorImg),
    url(r'^create_dataset$', app_views.create_dataset),
    url(r'^trainer$', app_views.trainer),
    url(r'^eigen_train$', app_views.eigenTrain),
    url(r'^detect$', app_views.detect),
    url(r'^detect/patient/$', app_views.pdetect,name='p_detect'),
    url(r'^detect_image$', app_views.detectImage),

    url(r'^record/$', app_views.NewRecord.as_view(),name='new_record'),

    url(r'^listrecord/$', app_views.RecordList.as_view(),name='list_record'),
    path('listrecord/detail/<int:pk>/', app_views.RecordDetails.as_view(),name='detail_record'),
    path('listrecord/detail/<int:pk>/edit/', app_views.RecordUpdate.as_view(),name='update_record'),

    url(r'^admin/', admin.site.urls),
    url(r'^records/', include('records.urls')),

]
