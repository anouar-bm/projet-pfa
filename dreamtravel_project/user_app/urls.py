from django.urls import path
from user_app.views import login
# from app_siteweb import views
app_name = 'user_app'
urlpatterns = [
    path("login_register", login),
]