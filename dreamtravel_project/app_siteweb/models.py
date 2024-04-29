from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractBaseUser
from django.utils.html import mark_safe
from django.core.validators import MinValueValidator, MaxValueValidator


def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class Admin(AbstractBaseUser):
    email = models.EmailField(_('email address'), unique=True)
    password = models.CharField(_('password'), max_length=128)
    username = models.CharField(_('username'), max_length=150, unique=True)
    username_field = "email"
    REQUIRED_FIELDS = ['username']
    def __str__(self):
        return self.username
    class Meta:
        db_table = 'admin'

def upload_to(instance, filename):
    return 'client_photos/{filename}'.format(instance.client.id, filename)


#class Client(abstractBaseUser):
class Client(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    photo = models.ImageField(upload_to='client_photos/', default='https://static.vecteezy.com/ti/vecteur-libre/p3/7296447-icone-utilisateur-dans-le-style-plat-icone-personne-symbole-client-vectoriel.jpg')
    USERNAME_FIELD = 'email'
    def __str__(self):
        return self.prenom
    def image_client(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.photo.url))

    class Meta:
        db_table = 'client'

class Like(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'like'

class Rating(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)  # Relation avec le client
    stars = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],  # Entre 1 et 5 étoiles
    )
    created_at = models.DateTimeField(auto_now_add=True)  # Date de création

    class Meta:
        db_table = 'rating'  # Nom de la table dans la base de données

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
    # image = models.ImageField(upload_to='villes/', blank=True, null=True)
    image = models.ImageField(upload_to='villes/', blank=True, null=True)

    class Meta:
        db_table = 'ville'
    def image_ville(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.photo.url))
    def __str__(self):
        return self.nom

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
    nom = models.CharField(max_length=25, default='Nom d\'hôtel inconnu')  # Ajout du champ nom
    emplacement = models.CharField(max_length=255)
    description = models.TextField(default='Aucune description fournie')  # Ajout du champ avec valeur par défaut
    num_telephone = models.CharField(max_length=15, default='+212000000000', validators=[RegexValidator(regex=r'^\+212\d{9}$')])
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    promo = models.DecimalField(max_digits=5, decimal_places=2, default=0)  # DecimalField for promo percentage
    photos = models.ManyToManyField('Image', related_name='hotels')
    likes = models.ManyToManyField(Like, related_name='hotel_likes', blank=True)
    reviews = models.ManyToManyField(Review, related_name='hotel_reviews', blank=True)
    class Meta:
        db_table = 'hotel'

    def calculate_total_price_with_promotion(self):
        if self.promo and self.promo > 0:
            discounted_price = self.prix * (1 - self.promo / 100)
            return discounted_price
        return self.prix

