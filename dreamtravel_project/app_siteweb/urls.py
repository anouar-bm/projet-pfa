from django.urls import path
from app_siteweb.views import index,home_page,essai_hotel,hotel_detail,activite_detail,restaurant_detail
# from app_siteweb import views
app_name = 'app_siteweb'
urlpatterns = [
    #path("home", home_page, name='homepage'),
    path("", index,name='index'),
    path("home", home_page, name='places'),
    path("mamounia", essai_hotel),
    path('hotel/<str:slug>',hotel_detail,name='hotel-detail'),
    path('activite/<str:slug>',activite_detail,name='activite-detail'),
    path('restaurant/<str:slug>',restaurant_detail,name='restaurant-detail'),
]

#from app_siteweb import views
#  path("", views.index),
    
