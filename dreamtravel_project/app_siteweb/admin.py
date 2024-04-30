from django.contrib import admin
from app_siteweb.models import *
# Register your models here.

class HotelAdmin(admin.ModelAdmin):
    list_display = ('nom','emplacement', 'num_telephone', 'prix', 'promo', 'calculate_total_price_with_promotion','slug')
    list_filter = ('emplacement', 'promo')
    search_fields = ('emplacement', 'num_tel')
# Enregistrer le modèle avec la classe `ModelAdmin`
admin.site.register(Hotel, HotelAdmin)

admin.site.register(Client)

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
admin.site.register(Admin)
