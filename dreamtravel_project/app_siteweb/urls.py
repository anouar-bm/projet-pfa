from django.urls import path
from app_siteweb.views import index
# from app_siteweb import views
app_name = 'app_siteweb'
urlpatterns = [
    path("", index),
]
