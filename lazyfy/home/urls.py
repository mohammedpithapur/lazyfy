from django.contrib import admin
from django.urls import path
# from requests import session
from .views import home

urlpatterns = [
    path('', home, name='home'),
    
]
