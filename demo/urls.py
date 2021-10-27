from django.urls import path
#from coderef.views import ProgTopicListView, ProgTopicDetailView
from .views import (
    DemoItemListView,
    DemoItemDetailSlugView
)

app_name = "demo"
urlpatterns = [
    path('', DemoItemListView.as_view(), name="list"),
    path('<slug>/', DemoItemDetailSlugView.as_view(), name="detail"),
]
