from django.db import models
from django.utils.translation import gettext_lazy as _

class Admin(models.Model):
    email = models.EmailField(_('email address'), unique=True)
    password = models.CharField(_('password'), max_length=128)
    username = models.CharField(_('username'), max_length=150, unique=True)

class Client(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

class Image(models.Model):
    image = models.ImageField(upload_to='restaurant_images/')

class Ville(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='villes/', blank=True, null=True)

class Restaurant(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    images = models.ManyToManyField(Image, related_name='restaurants')
    
class Activite(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    images = models.ManyToManyField(Image, related_name='activites')
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    duree = models.CharField(max_length=100)
    emplacement = models.CharField(max_length=255)
    num_telephone = models.CharField(max_length=15, help_text="Le numéro de téléphone doit commencer par +212")

class Hotel(models.Model):
    emplacement = models.CharField(max_length=255)
    num_tel = models.CharField(max_length=15, help_text="Le numéro de téléphone doit commencer par +212")
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    promo = models.BooleanField(default=False)
    photos = models.ManyToManyField('Image', related_name='hotels')

