import json
import os
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.conf import settings
from django.views.generic import (
    ListView,
    DetailView
)
#from .models import ResourceFile,Schema

#BASE_DIR = settings.BASE_DIR

# Create your views here.
def home(request):
    template_name="apps/tweetme/home.html"
    appname="TweetMe"
    context={
        "appname":appname
    }
    print(f"context {context}")
    return render(request,template_name,context)

def react_spa(request):
    template_name="apps/tweetme/react_spa.html"
    appname="TweetMe"
    context={
        "appname":appname
    }
    print(f"context {context}")
    return render(request,template_name,context)