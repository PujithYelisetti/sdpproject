from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('mail', views.send_emails, name='send_emails'),
]
