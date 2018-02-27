import requests, datetime, math


from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


from .models import Values, ConverterHistory

# Create your views here.
def fetch(request):
    #Fetching API data and storing to database!
    response = requests.get('https://api.fixer.io/latest')
    values = response.json()
    Values.objects.all().delete()
    for key,val in values['rates'].items():
        temp=Values(name=key, value=val)
        temp.save()
    temp = Values(name='EUR', value=1.0)
    temp.save()

    return redirect('home')

def home(request):
    #Extracting previous history if user is authenticated,else returning empty string
    if request.user.is_authenticated:
        history = ConverterHistory.objects.filter(user_name=request.user)
    else:
        history = ""

    return render(request, 'home.html', {
        'currency' : Values.objects.all(),
        'convertedValue' : 0,
        'history' : history,
        })


def convert(request):
    # Extracting values from form
    fromCurrency = request.POST.get('fromCurrency')
    toCurrency = request.POST.get('toCurrency')
    value = float(request.POST.get('value'))
    dateNow = datetime.datetime.now()
    convertedVal = 0
    historyString = str(value) + " " + fromCurrency + " to " + toCurrency + " on " + dateNow.strftime("%d-%m-%Y")
    #Saving Conversion history
    temp = ConverterHistory(user_name = request.user, history = historyString)
    temp.save()
    #Conversion Logic and Rendering
    if fromCurrency == toCurrency:
        convertedVal = value
    elif fromCurrency == 'EUR':
        convertedVal = value * (Values.objects.get(name = toCurrency).value)
    else:
        convertedToEur = value / (Values.objects.get(name = fromCurrency).value)
        convertedVal = convertedToEur * (Values.objects.get(name = toCurrency).value)

    outputString = str(value) + " " + fromCurrency + " = " + str(round(convertedVal, 2)) +" " +toCurrency
    return render(request, 'home.html', {
        'currency' : Values.objects.all(),
        'history' : ConverterHistory.objects.filter(user_name=request.user),
        'outputString' : outputString
    })
