from django.http import HttpResponse
from django.shortcuts import render
from app_siteweb.models import Hotel, PlaceTouristique, Activite, Restaurant

def index(request):
    return render(request, 'accueil/index.html')

def login(request):
    return render(request, 'accueil/login-register.html')

def home_page(request):
    Hotels = Hotel.objects.all()
    Place_Touristique = PlaceTouristique.objects.all()
    activites = Activite.objects.all()
    restaurants = Restaurant.objects.all()
    context = {
        'hotels': Hotels,
        'places_touristiques': Place_Touristique,
        # 'activites': activites,
        'restaurants': restaurants
    }
    return render(request, 'accueil/home.html', context)

# def list_hotels(request):
#     hotels = Hotel.objects.all()  # Obtenez tous les hôtels
#     return render(request, 'hotel_list.html', {'hotels': hotels})  # Rendre le template avec les hôtels


def Atlas(request):
    return render(request, 'accueil/atlass.html')


# Create your views here.
