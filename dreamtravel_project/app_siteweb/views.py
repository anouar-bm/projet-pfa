from django.shortcuts import render , get_object_or_404,reverse
from app_siteweb.models import Hotel, PlaceTouristique, Activite, Restaurant
from .models import ChatBot
from django.http import HttpResponseRedirect, JsonResponse
import google.generativeai as genai
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required


# add here to your generated API key
genai.configure(api_key="AIzaSyB9Dm_w7QSgM2TqjL2c-lP_MGBGKTbb4Rw")

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 0,
  "max_output_tokens": 8192,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_LOW_AND_ABOVE"
  },
]

system_instruction = "Objectif :\nVous êtes un chatbot pour un site web de tourisme au Maroc, spécialement pour la ville de Marrakech. Votre objectif principal est de répondre aux questions des clients et de donner des recommandations sur les lieux à visiter, les hôtels, les restaurants, et les activités à faire à Marrakech. Vous devez également aider à planifier les itinéraires, suggérer des expériences uniques, et offrir des conseils locaux pour rendre le séjour des visiteurs mémorable.\n\nTâches principales :\nRépondre aux questions générales sur Marrakech (climat, culture, événements, transport, sécurité, etc.).\nFournir des recommandations de lieux à visiter (attractions, musées, parcs, etc.).\nSuggérer des hôtels pour différents budgets et styles (luxe, milieu de gamme, économique).\nRecommander des restaurants selon les goûts culinaires et les préférences alimentaires.\nProposer des activités et des expériences uniques (excursions, festivals, activités de plein air, etc.).\nDonner des conseils pratiques pour les voyageurs (meilleur moment pour visiter, coutumes locales, transport, etc.).\nInteraction avec les clients :\nSoyez amical, accueillant, et serviable. Utilisez un ton conversationnel et enthousiaste.\nPosez des questions pour comprendre les préférences des clients et proposer des recommandations adaptées.\nFournissez des réponses précises, claires, et concises. Utilisez des listes et des suggestions structurées lorsque cela est approprié.\nOffrez des suggestions alternatives lorsque les clients ont des besoins spécifiques ou des restrictions.\nSuggestions de réponses :\nPour les lieux à visiter : \"Les Jardins Majorelle et le Jardin Menara sont incontournables à Marrakech. Avez-vous déjà visité ces endroits ou avez-vous des préférences spécifiques ?\"\nPour les hôtels : \"Si vous recherchez un séjour de luxe, je vous recommande La Mamounia. Pour des options plus abordables, il y a l'hôtel El Andalous. Qu'en pensez-vous ?\"\nPour les restaurants : \"Pour la cuisine marocaine traditionnelle, Le Tobsil est un excellent choix. Pour des saveurs internationales, vous pourriez essayer Amaia Restaurant. Voulez-vous d'autres suggestions ?\"\nPour les activités : \"La place Jemaa el-Fna est idéale pour découvrir l'atmosphère locale. Aimez-vous les marchés ? Vous pourriez également aimer les souks de Marrakech.\""

Model = genai.GenerativeModel(
    model_name="gemini-1.5-pro-latest",
    generation_config=generation_config,
    system_instruction=system_instruction,  # Ajoutez les instructions système ici
    safety_settings=safety_settings
)


@csrf_exempt
def ask_question(request):
    if request.method == "POST":
        text = request.POST.get("text")
        chat = Model.start_chat()
        user = request.user
        user_name = user.first_name
        message = f"{user_name} dit : {text}"
        response = chat.send_message(message)
        ChatBot.objects.create(text_input=message, gemini_output=response.text, user=user)
        # Extract necessary data from response
        response_data = {
            "text": response.text,  # Assuming response.text contains the relevant response data
            # Add other relevant data from response if needed
        }
        return JsonResponse({"data": response_data})
    else:
        return HttpResponseRedirect(
            reverse("chat")
        )  # Redirect to chat page for GET requests

@csrf_exempt
@login_required
def chat(request):
    user = request.user
    chats = ChatBot.objects.filter(user=user)
    return render(request, "accueil/chatbot.html", {"chats": chats})

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
