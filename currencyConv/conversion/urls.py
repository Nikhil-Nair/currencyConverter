from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.fetch, name='fetch'),
    path('home', views.home, name='home'),
    path('convert', views.convert, name='convert'),
]
