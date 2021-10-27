from django.urls import path

from .views import (
    PostAPIView,
    PostAPIDetailView,
)

app_name = 'posts-api'
urlpatterns = [
    path("",PostAPIView.as_view()),
    path("<slug>/",PostAPIDetailView.as_view(),name="detail"),
]
