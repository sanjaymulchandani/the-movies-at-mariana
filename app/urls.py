from django.urls import path
from .views import movie_details

urlpatterns = [
    path('movie-details/', movie_details, name='movie_details'),
]
