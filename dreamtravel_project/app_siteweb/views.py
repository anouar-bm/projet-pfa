from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'accueil/index.html')

def login(request):
    return render(request, 'accueil/login-register.html')


# Create your views here.
