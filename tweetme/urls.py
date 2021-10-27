from django.urls import path

from .views import (
    home,
    react_spa
)

app_name="tweetme"
urlpatterns = [
    path('home',home,name="home"),
    path('',react_spa,name="react_spa")
]