from django.shortcuts import render , get_object_or_404,reverse
from app_siteweb.models import Hotel, PlaceTouristique, Activite, Restaurant
from .models import ChatBot
from django.http import HttpResponseRedirect, JsonResponse
import google.generativeai as genai



def index(request):
    return render(request, 'accueil/index.html')

def home_page(request):
    Hotels = Hotel.objects.all()
    Place_Touristique = PlaceTouristique.objects.all()
    activites = Activite.objects.all()
    restaurants = Restaurant.objects.all()
    context = {
        'hotels': Hotels,
        'places_touristiques': Place_Touristique,
        'activites': activites,
        'restaurants': restaurants
    }
    return render(request, 'accueil/home.html', context)

def essai_hotel(request):
    return render(request, 'accueil/mamounia.html')

def hotel_detail(request, slug):
    hotel=get_object_or_404(Hotel, slug=slug)
    return render(request, 'accueil/hotel_detail.html',context={"hotel":hotel})

def activite_detail(request, slug):
    activite = get_object_or_404(Activite, slug=slug)
    return render(request, 'accueil/activite_detail.html',context={"activite":activite})
    
def restaurant_detail(request, slug):
    restaurant = get_object_or_404(Restaurant, slug=slug)
    return render(request, 'accueil/restaurant_detail.html',context={"restaurant":restaurant})



# def list_hotels(request):
#     hotels = Hotel.objects.all()  # Obtenez tous les hôtels
#     return render(request, 'hotel_list.html', {'hotels': hotels})  # Rendre le template avec les hôtels


def Atlas(request):
    return render(request, 'accueil/atlass.html')


# Create your views here.
