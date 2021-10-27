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
    template_name="apps/htmlcss/home.html"
    appname="HtmlCss"
    context={
        "appname":appname
    }
    print(f"context {context}")
    return render(request,template_name,context)

def boxmodel(request):
    template_name="apps/htmlcss/boxmodel.html"
    pgname="TheBox Model"
    context={
        "pgname":pgname
    }
    print(f"context {context}")
    return render(request,template_name,context)

def selectors(request):
    template_name="apps/htmlcss/selectors.html"
    pgname="CSS Selectors"
    context={
        "pgname":pgname
    }
    print(f"context {context}")
    return render(request,template_name,context)

def colors(request):
    template_name="apps/htmlcss/colors.html"
    pgname="Colors"
    context={
        "pgname":pgname
    }
    print(f"context {context}")
    return render(request,template_name,context)

def layout(request):
    template_name="apps/htmlcss/layout.html"
    pgname="Layout"
    context={
        "pgname":pgname
    }
    print(f"context {context}")
    return render(request,template_name,context)