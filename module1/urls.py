from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('hello/',hello,name = 'hello'),
    path('',newhomepage,name ='newhomepage'),
    path('travelpackage/',travelpackage,name="travelpackage"),
    path('print/',print1,name="print"),
    path('print_to_console1/',print_to_console,name='print_to_console1'),
    path('callrandomotp/',randomcall,name='randomcall'),
    path('printotpconsole/',RandomOTPgenerator,name='RandomOTPgenerator'),
    path('date/',get_date,name='get_date'),
    path("dateu/",getdate,name="getdate"),
    path('register/',registercall,name='register'),
    path('registerloginfunction/',registerloginfunction,name='Pujith'),
    path('pie_chart/',pie_chart,name='pie_chart'),
    path('weather',weatherpagecall,name='weatherpagecall'),
    path('weathers',weatherlogic,name='weatherlogic'),
    path('feedback/',feedback,name='feedback'),
    path('mainfeedback/',mainfeedback,name='mainfeedback'),
    path('login/',login,name='login'),
    path('signup/',signup,name='signup'),
]