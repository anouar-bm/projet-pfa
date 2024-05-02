from django.contrib import admin
from app_siteweb.models import *
# Register your models here.

class chatbotAdmin(admin.ModelAdmin):
    list_display = ('user','text_input', 'gemini_output', 'date')
    search_fields = ['text_input']
admin.site.register(ChatBot, chatbotAdmin)


class HotelAdmin(admin.ModelAdmin):
    list_display = ('nom','emplacement', 'num_telephone', 'prix', 'promo', 'calculate_total_price_with_promotion','slug')
    list_filter = ('emplacement', 'promo')
    search_fields = ('emplacement', 'num_tel')
# Enregistrer le modèle avec la classe `ModelAdmin`
admin.site.register(Hotel, HotelAdmin)

class ClientAdmin(admin.ModelAdmin):
    # Champs à afficher dans la liste des clients
    list_display = ('nom', 'user', 'photo', 'user_full_name')

    # Champs cliquables qui mènent à la vue de détail
    list_display_links = ('nom', 'user')

    # Champs disponibles pour la recherche
    search_fields = ('nom', 'user__first_name', 'user__last_name')

    # Ajouter des filtres sur le côté de la page d'administration
    list_filter = ('user',)

    # Définir une méthode pour afficher le nom complet de l'utilisateur
    def user_full_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"

    # Nom de la colonne pour `user_full_name`
    user_full_name.short_description = 'Nom Complet de l\'Utilisateur'


# Enregistrer le modèle Client avec la classe ClientAdmin
admin.site.register(Client, ClientAdmin)


class villeAdmin(admin.ModelAdmin):
    list_display = ['nom']
    search_fields = ['nom']
admin.site.register(Ville, villeAdmin)


class PlaceTouristiqueAdmin(admin.ModelAdmin):
    list_display = ('nom', 'description', 'ville')  # Colonnes affichées
    search_fields = ['nom']
admin.site.register(PlaceTouristique, PlaceTouristiqueAdmin)

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('nom','description','rating','slug')
    search_fields = ['nom']
admin.site.register(Restaurant, RestaurantAdmin)

class ActiviteAdmin(admin.ModelAdmin):
    list_display = ('nom','description','duree','slug')
    search_fields = ['nom']

admin.site.register(Activite, ActiviteAdmin)
admin.site.register(Like)
admin.site.register(Review)
admin.site.register(Image)
# admin.site.register(Admin)
