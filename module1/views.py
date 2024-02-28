import string
import random

from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello(request):
    return HttpResponse("<center>Welcome to TTM Homepage</center>")
def newhomepage(request):
    return render(request,'newHomepage.html')

def travelpackage(request):
    return render(request,'travelpackage.html')

def print1(request):
    return render(request,'print_to_console1.html')
def print_to_console(request):
    if request.method == "POST":
        user_input = request.POST['user_input']
        print(f'Use input:{user_input}')
        #return HttpResponse('From submitted successfully')
        a1 ={'user_input':user_input}
        return render(request,'print_to_console1.html',a1)

def randomcall(request):
        return render(request, 'RandomOTPgenerator.html')

def RandomOTPgenerator(request):
        if request.method == "POST":
            user_input = request.POST['user_input']
            print(f'Use input:{user_input}')
            # return HttpResponse('From submitted successfully')
            a2 =int(user_input)
            ran1 =''.join(random.sample(string.digits,k=a2))
            a1 = {'ran1': ran1}
            return render(request, 'RandomOTPgenerator.html', a1)

import datetime
from django.shortcuts import render
from .forms import *

def getdate(request):
    return render(request,'get_date.html')


def get_date(request):
    if request.method=='POST':
        form=IntegerDateForm(request.POST)
        if form.is_valid():
            integer_value=form.cleaned_data['integer_value']
            date_value=form.cleaned_data['date_value']
            updated_date= date_value + datetime.timedelta(days=integer_value)
            return render(request,'get_date.html',{'updated_date':updated_date})
        else :
            form=IntegerDateForm()
        return render(request,'get_date.html',{'form':form})


#regidster
def registercall(request):
    return render(request,'Pujith.html')

from .models import *
from django.shortcuts import render,redirect
def registerloginfunction(request):
    if request.method =='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phonenumber = request.POST.get('phonenumber')

        #check for existing email
        if register.objects.filter(email=email).exists():
            return HttpResponse("Email already registered")
        #create new register
        register.objects.create(name=name,email=email,password=password,phonenumber=phonenumber)
        return redirect('newHomepage')
    return render(request,'Pujith.html')

import matplotlib.pyplot as plt
import numpy as np

def pie_chart(request):
    if request.method == 'POST':
        form = PieChartForm(request.POST)
        if form.is_valid():
            # Process user input
            y_values = [int(val) for val in form.cleaned_data['y_values'].split(',')]
            labels = [label.strip() for label in form.cleaned_data['labels'].split(',')]

            # Create pie chart
            plt.pie(y_values, labels=labels, startangle=90)
            plt.savefig('static/images/pie_chart.png')  # Save the chart image
            img1={'chart_image': '/static/images/pie_chart.png'}
            return render(request, 'chart_form.html', img1)
    else:
        form = PieChartForm()
    return render(request, 'chart_form.html', {'form': form})



class PieChartForm(forms.Form):
    y_values = forms.CharField(label='Y Values', help_text='Enter comma-separated values')
    labels = forms.CharField(label='Labels', help_text='Enter comma-separated labels')

import requests
def weatherpagecall(request):
    return render(request,'weatherappinput.html')


def weatherlogic(request):
    if request.method == 'POST':
        place = request.POST['place']
        API_KEY = '4b3db005983fbd3bf693850b2b35aa944b3db005983fbd3bf693850b2b35aa94'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={place}&appid={API_KEY}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            temperature1= round(temperature - 273.15,2)
            return render(request, 'weatherappinput.html',
                          {'city': str.upper(place), 'temperature1': temperature1, 'humidity': humidity})
        else:
            error_message = 'City not found. Please try again.'
            return render(request, 'weatherappinput.html', {'error_message': error_message})

def feedback(request):
    return render(request,'feedback.html')

def mainfeedback(request):
        if request.method == 'POST':
            FirstName = request.POST.get('FirstName')
            LastName = request.POST.get('LastName')
            Email = request.POST.get('Email')
            Comment = request.POST.get('Comment')
            Feedback.objects.create(FirstName=FirstName,  LastName=LastName, Email=Email, Comment=Comment)
            send_mail(
                'Thank you for your feedback',
                Comment,
                '2200031352cseh@gmail.com',
                [Email],
                fail_silently=False,
            )
        return HttpResponse("<h3><center>Thank You For Your FeedBack a Mail has sent to You!")
def login(request):
    return render(request,'login.html')

def signup(request):
    return render(request,'signup.html')

import auth
def login1(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,'newHomepage.html')
        else :
            messages.error(request,'Invalid Credentials')
            return render(request,'login.html')
    else:
        return render(request,'login.html')

