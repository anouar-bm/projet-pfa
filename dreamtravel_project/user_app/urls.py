from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .forms import LoginForm
from django.contrib.auth.views import LogoutView

app_name = 'user_app'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', LogoutView.as_view(http_method_names=['post']), name='logout'),  # Accepter POST uniquement
]
