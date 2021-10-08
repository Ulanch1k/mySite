from django.urls import path
from .views import create_film

movie_urlpatterns = {
    path('product/', create_film)
}