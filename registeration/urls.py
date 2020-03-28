from django.contrib import admin
from django.urls import re_path,include
from . import views
app_name = 'registeration'
urlpatterns = [
    re_path(r'^$', views.index,name = 'index'),
    re_path(r'^register/',views.register,name='register'),
]
