import json
#django imports
from django.conf import settings
from django.db.models import query
from django.views.generic import View
from django.shortcuts import get_object_or_404, render,redirect
from django.http import JsonResponse,HttpResponse, Http404
#REST
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework import (
    authentication, 
    permissions,
    generics, 
    mixins,
)

from django.contrib.auth.models import User


ALLOWED_HOSTS = settings.ALLOWED_HOSTS

# rest


from .serializers import (
    GenreSerializer,
    MovieSerializer,
)
from vidly.models import (
    Genre,
    Movie
)

class MovieAPIView(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    generics.ListAPIView):
    #permission_classes = []
    #authentication_classes = []
    serializer_class        = MovieSerializer
    #pagination_class    = CPATAPIPagination
    #queryset = Function.objects.all()
 

    def get_queryset(self):
        request = self.request
        qs = Movie.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(name__icontains=query)
        return qs

    def post(self, request, *args, **kwargs): 
        return self.create(request, *args, **kwargs)


class MovieAPIDetailView(
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.RetrieveAPIView):
    #permission_classes      = []
    #authentication_classes  = []
    serializer_class        = MovieSerializer
    queryset                = Movie.objects.all()
    lookup_field            = 'id'
 
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
 
    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
 
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



class GenreAPIView(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    generics.ListAPIView):
    #permission_classes = []
    #authentication_classes = []
    serializer_class            = GenreSerializer
    #queryset = Function.objects.all()
 
    def post(self, request, *args, **kwargs): 
        return self.create(request, *args, **kwargs)

    def get_queryset(self):
        request = self.request
        qs = Genre.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(syntax__icontains=query)
        return qs



class GenreAPIDetailView(
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.RetrieveAPIView):
    permission_classes      = []
    authentication_classes  = []
    serializer_class        = GenreSerializer
    queryset                = Genre.objects.all()
    lookup_field            = 'pk'
 
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
 
    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
 
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


@api_view(['POST']) # http method the client == POST
# @authentication_classes([SessionAuthentication, MyCustomAuth])
@permission_classes([IsAuthenticated]) # REST API course
def courseitem_api_create_view(request, *args, **kwargs):
    serializer = CourseItemSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return JsonResponse(serializer.data, status=201)
    return JsonResponse({}, status=400)



def get_paginated_queryset_response(qs, request):
    paginator = PageNumberPagination()
    paginator.page_size = 20
    paginated_qs = paginator.paginate_queryset(qs, request)
    serializer = CourseItemSerializer(paginated_qs, many=True, context={"request": request})
    return paginator.get_paginated_response(serializer.data) # Response( serializer.data, status=200)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def courseitem_feed_view(request, *args, **kwargs):
    user = request.user
    qs = CourseItem.objects.feed(user)
    return get_paginated_queryset_response(qs, request)


@api_view(['GET'])
def courseitem_api_list_view(request, *args, **kwargs):
    qs = CourseItem.objects.all()
    username = request.GET.get('username') # ?username=Justin
    if username != None:
        qs = qs.by_username(username)
    return get_paginated_queryset_response(qs, request)


@api_view(['GET'])
def courseitem_detail_view(request, tweet_id, *args, **kwargs):
    qs = CourseItem.objects.filter(id=tweet_id)
    if not qs.exists():
        return Response({}, status=404)
    obj = qs.first()
    serializer = CourseItemSerializer(obj)
    return Response(serializer.data, status=200)


@api_view(['DELETE', 'POST'])
@permission_classes([IsAuthenticated])
def courseitem_delete_view(request, course_item_id, *args, **kwargs):
    qs = CourseItem.objects.filter(id=course_item_id)
    if not qs.exists():
        return Response({}, status=404)
    qs = qs.filter(user=request.user)
    if not qs.exists():
        return Response({"message": "You cannot delete this tweet"}, status=401)
    obj = qs.first()
    obj.delete()
    return Response({"message": "Tweet removed"}, status=200)


# @api_view(['POST'])
# #@permission_classes([IsAuthenticated])
# def course_action_view(request, *args, **kwargs):
#     '''
#     id is required.
#     Action options are: like, unlike, retweet
#     '''
#     serializer = CourseActionSerializer(data=request.data)
#     if serializer.is_valid(raise_exception=True):
#         data = request.data
#         print(f"CALLED course action api detail view...{request} \nargs {args} \nkwargs {kwargs} \nDATA {data}")
#         courseSlug = data.get("slug")
#         action = data.get("action")
#         qs = Course.objects.filter(slug=courseSlug)
#         if not qs.exists():
#             return JsonResponse({},status=404)
#         obj = qs.first()
#         if action == "like":
#             obj.likes.add(request.user)
#             serializer=CourseSerializer(obj)
#             return JsonResponse(serializer.data,status=200)
#         if action == "unlike":
#             obj.likes.remove(request.user)
#             serializer=CourseSerializer(obj)
#             return JsonResponse(serializer.data,status=200)
#         elif action == "complete":
#             obj.user_course_completed.add(request.user)
#             serializer=CourseSerializer(obj)
#             return JsonResponse(serializer.data,status=200)
#     return Response({}, status=200)
