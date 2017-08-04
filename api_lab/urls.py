from django.conf.urls import url, include
from django.contrib import admin
from . import views
from .submodule import views as view_submodule

urlpatterns = [
    url(r'^home/$', views.home),
    url(r'^api/$', views.derta),
    url(r'^product/$', views.product),
    url(r'^traditional_logging/$', views.traditional_logging),
    url(r'^get_list_uber_product/$', views.get_list_uber_product),
    url(r'^submodule/$', view_submodule.example_method),
    url(r'^usage_model/$', views.use_model),


]