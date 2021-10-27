from django.urls import path

from .views import (
    MovieAPIView, 
    MovieAPIDetailView,
    GenreAPIView,
    GenreAPIDetailView,
)

urlpatterns = [
    path('movies/',MovieAPIView.as_view()),
    path('movies/<id>/',MovieAPIDetailView.as_view()),
    path('genre/',GenreAPIView.as_view()),
    path('genre/<id>/',GenreAPIDetailView.as_view()),
]