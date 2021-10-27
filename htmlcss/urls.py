from django.urls import path

from .views import (
    home,
    boxmodel,
    selectors,
    colors,
    layout
)

app_name="htmlcss"
urlpatterns = [
    path('',home,name="home"),
    path('boxmodel/',boxmodel,name="boxmodel"),
    path('selectors/',selectors,name="selectors"),
    path('colors/',colors,name="colors"),
    path('layout/',layout,name="layout")
]