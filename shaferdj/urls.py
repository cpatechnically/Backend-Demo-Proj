from django.urls import path

from .views import (
    home
)

app_name="shaferdj"
urlpatterns = [
    path('',home,name="home")
]