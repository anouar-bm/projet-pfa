from django.http import HttpResponse
from django.shortcuts import render
from app_siteweb.models import Hotel

def index(request):
    return render(request, 'accueil/index.html')

def login(request):
    return render(request, 'accueil/login-register.html')

def dict_hotels(request):
    hotels = Hotel.objects.all()

    return render(request, 'accueil/hotels.html', {'hotel': hotels})

def Atlas(request):
    return render(request, 'accueil/atlass.html')


# Create your views here.
