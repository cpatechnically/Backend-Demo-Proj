from django.urls import path

from .views import (
    react_spa
)

app_name="captures"
urlpatterns = [
    path("",react_spa,name="react_spa"),
]
