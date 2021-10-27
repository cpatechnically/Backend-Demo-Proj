from django.shortcuts import render

# Create your views here.
import json
from django.http.response import Http404
from django.shortcuts import get_object_or_404, render,redirect
from django.utils.http import is_safe_url
from django.http import JsonResponse
from django.conf import settings
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.
def react_spa(request):
    template_name="apps/captures/react_spa.html"
    pgname = "React Home"
    sbtext = "Welcome! "

    items = [
        {"id":1,"name":"Annoucements!"},
        {"id":2,"name":sbtext},
        {"id":3,"name":pgname},
    ]
    context={
        "sidebar_list":items
    }
    print(f"context {context}")
    return render(request,template_name,context)

