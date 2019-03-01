from django.contrib import admin
from django.urls import path
from Main import views

urlpatterns = [
    path('', views.home, name='home'),
    path('main/home/', views.home, name='home'),
]
