# sendemail/urls.py
from django.contrib import admin
from django.urls import path

from .views import successView
app_name = 'email'
urlpatterns = [
    # path('email/', emailView, name='email'),
    path('success/', successView, name='success'),
]
