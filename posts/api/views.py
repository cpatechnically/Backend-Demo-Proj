from rest_framework import authentication, generics, permissions
#django imports
from django.views.generic import View
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from django.contrib.auth.models import User
from cap.permissions import IsOwnerOrReadOnly

# rest
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework import (
    authentication, 
    permissions,
    generics, 
    mixins
)
from posts.models import Post
from .serializers import PostSerializer


class PostAPIView(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    generics.ListAPIView):
    #permission_classes  = []
    #authentication_classes      = []
    serializer_class            = PostSerializer
        
    def get_queryset(self):
        request = self.request
        qs = Post.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(email__icontains=query)
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)



class PostAPIDetailView(
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.RetrieveAPIView):
    permission_classes  = [permissions.IsAuthenticatedOrReadOnly]
    #authentication_classes      = []
    serializer_class            = PostSerializer
    queryset                    = Post.objects.all()
    lookup_field                = 'slug'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)