from django.urls import path
from . import views
app_name = 'scraping_app'
urlpatterns = [
    path('', views.home, name='home'),
    path('scrape/', views.scrape, name='scrape'),
    path('download/', views.download_file, name='download_file'),
    # Ensure a URL pattern for the redirect exists
    path('results/', views.scrape_results, name='scrape_results'),  # Add this
]
