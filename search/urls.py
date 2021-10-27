from django.urls import path
#from coderef.views import ProgTopicListView, ProgTopicDetailView
from .views import SearchView

app_name = "search"
urlpatterns = [
    path('', SearchView.as_view(), name="query"),
]
