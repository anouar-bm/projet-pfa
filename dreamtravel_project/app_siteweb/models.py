from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator

class Admin(models.Model):
    email = models.EmailField(_('email address'), unique=True)
    password = models.CharField(_('password'), max_length=128)
    username = models.CharField(_('username'), max_length=150, unique=True)
    class Meta:
        db_table = 'admin'

class Client(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    photo = models.ImageField(upload_to='client_photos/', default='https://static.vecteezy.com/ti/vecteur-libre/p3/7296447-icone-utilisateur-dans-le-style-plat-icone-personne-symbole-client-vectoriel.jpg')
    class Meta:
        db_table = 'client'

class Like(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'like'

class Review(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'review' 
        
class Image(models.Model):
    image = models.ImageField(upload_to='image_places/')

class Ville(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='villes/', blank=True, null=True)
    class Meta:
        db_table = 'ville'

class PlaceTouristique(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='places_touristiques/', blank=True, null=True)
    ville = models.ForeignKey(Ville, on_delete=models.CASCADE, related_name='places_touristiques')

    class Meta:
        db_table = 'place_touristique'

class Restaurant(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    images = models.ManyToManyField(Image, related_name='restaurants')
    likes = models.ManyToManyField(Like, related_name='restaurant_likes', blank=True)
    reviews = models.ManyToManyField(Review, related_name='restaurant_reviews', blank=True)

    class Meta:
        db_table = 'restaurant'

class Activite(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    images = models.ManyToManyField(Image, related_name='activites')
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    duree = models.CharField(max_length=100)
    emplacement = models.CharField(max_length=255)
    num_telephone = models.CharField(max_length=15, validators=[RegexValidator(regex=r'^\+212\d{9}$', message="Le numéro de téléphone doit commencer par +212")], help_text="Le numéro de téléphone doit commencer par +212")
    likes = models.ManyToManyField(Like, related_name='activite_likes', blank=True)
    reviews = models.ManyToManyField(Review, related_name='activite_reviews', blank=True)

    class Meta:
        db_table = 'activite'

class Hotel(models.Model):
    emplacement = models.CharField(max_length=255)
    num_tel = models.CharField(max_length=15, validators=[RegexValidator(regex=r'^\+212\d{9}$', message="Le numéro de téléphone doit commencer par +212")], help_text="Le numéro de téléphone doit commencer par +212")
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    promo = models.DecimalField(max_digits=5, decimal_places=2, default=0)  # DecimalField for promo percentage
    photos = models.ManyToManyField('Image', related_name='hotels')
    likes = models.ManyToManyField(Like, related_name='hotel_likes', blank=True)
    reviews = models.ManyToManyField(Review, related_name='hotel_reviews', blank=True)
    class Meta:
        db_table = 'hotel'

    def calculate_total_price_with_promotion(self):
     
        discounted_price = self.prix * (1 - self.promo / 100)  # Calculate discounted price based on promo percentage
        return discounted_price
    

