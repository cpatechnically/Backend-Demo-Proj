from rest_framework import authentication, generics, permissions
#django imports
from django.views.generic import View
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from django.contrib.auth.models import User

# rest
# from rest_framework.views import APIView
# from rest_framework.response import Response
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework import (
    authentication, 
    permissions,
    generics, 
    mixins
)
from captures.models import EmailCapture
from .serializers import EmailCaptureSerializer

# django corsheaders cfe.sh
class EmailCaptureCreateAPIView(generics.CreateAPIView):
    queryset            = EmailCapture.objects.all()
    serializer_class    = EmailCaptureSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.AllowAny]
    def perform_create(self, serializer):
        request = self.request
        user = request.user
        if not user.is_authenticated:
            user = None # Annon User
        serializer.save(user=user)



class EmailCaptureAPIView(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    generics.ListAPIView):
    #permission_classes          = []
    #authentication_classes      = []
    serializer_class            = EmailCaptureSerializer
        
    def get_queryset(self):
        request = self.request
        qs = EmailCapture.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(email__icontains=query)
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class EmailCaptureAPIDetailView(
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.RetrieveAPIView):
    #permission_classes          = []
    #authentication_classes      = []
    serializer_class            = EmailCaptureSerializer
    #queryset                    = EmailCapture.objects.all()
    lookup_field                = 'email'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)