from django.contrib import admin
from app_siteweb.models import *
# Register your models here.
# class ClientAdmin(Client.Clientadmin):
#   list_display = ('nom', 'prenom', 'email', 'photo')
admin.site.register(Client)
admin.site.register(Ville)
admin.site.register(PlaceTouristique)
admin.site.register(Restaurant)
admin.site.register(Hotel)
admin.site.register(Activite)
admin.site.register(Like)
admin.site.register(Review)
admin.site.register(Image)
admin.site.register(Admin)
