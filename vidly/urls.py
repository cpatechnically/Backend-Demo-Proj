from django.urls import path

from .views import (
    react_spa
)

app_name="vidly"
urlpatterns = [
    path('',react_spa,name="react_spa")
]