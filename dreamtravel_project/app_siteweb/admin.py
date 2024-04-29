from django.contrib import admin
from app_siteweb.models import Client
# Register your models here.
# admin.site.register(Client) :
class ClientAdmin(Client.Clientadmin):
  list_display = ('nom', 'prenom', 'email', 'photo')
admin.site.register(Client, ClientAdmin)