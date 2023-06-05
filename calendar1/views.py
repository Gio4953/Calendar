from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def calendar1_view(request, year, month, number):
    response = f"Date: {year}-{month}-{number}"
    return HttpResponse(response)

def home_view(request):
    return render(request, 'calendar1/templates/calendar1/home.html')
