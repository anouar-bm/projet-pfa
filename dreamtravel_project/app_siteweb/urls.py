from django.urls import path
from app_siteweb.views import index,home_page
# from app_siteweb import views
app_name = 'app_siteweb'
urlpatterns = [
    path("", index),
    path("home", home_page, name='home'),
]

#from app_siteweb import views
#  path("", views.index),
    
