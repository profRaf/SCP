from django.contrib import admin
from django.urls import path
from Supplementary import views

urlpatterns = [
    path('supplementary/health_check/', views.health_check, name='health_check'),
]
