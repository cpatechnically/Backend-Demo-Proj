from django.urls import path, re_path

from .views import (
    react_spa
    )


app_name = 'cfereact'
urlpatterns = [
    path('',react_spa, name='react_spa'),
]