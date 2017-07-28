from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^home/$', views.home),
    url(r'^api/$', views.derta),
    url(r'^product/$', views.product),
    url(r'^traditional_logging/$', views.traditional_logging),

]