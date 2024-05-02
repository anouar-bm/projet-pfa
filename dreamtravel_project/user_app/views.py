from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignupForm
from app_siteweb.models import Client

# Create your views here.

def signup(request):
    if request.method == 'POST':
        # Traitez les données POST et les fichiers téléchargés
        form = SignupForm(request.POST, request.FILES)

        if form.is_valid():
            # Sauvegardez le nouvel utilisateur
            user = form.save()

            # Création d'un nouvel objet Client lié à cet utilisateur
            client = Client(
                nom=form.cleaned_data.get('first_name') + ' ' + form.cleaned_data.get('last_name'),  # Prénom + Nom de famille
                user=user,  # Associez le client à l'utilisateur nouvellement créé
                photo=form.cleaned_data.get('image')  # Si une image a été téléchargée
            )

            client.save()  # Sauvegardez le nouveau client

            # Connectez l'utilisateur nouvellement créé
            login(request, user)

            # Redirection après inscription réussie
            return redirect('user_app:login')  # Ajustez le chemin de redirection selon vos besoins
    else:
        form = SignupForm()

    return render(request, 'user/signup.html', {
        'form': form
    })
