from django.urls import path

from .views import (
    EmailCaptureAPIView,
    EmailCaptureAPIDetailView,
)


urlpatterns = [
    path("caps/",EmailCaptureAPIView.as_view()),
    path("caps/<email>/",EmailCaptureAPIDetailView.as_view()),
]
