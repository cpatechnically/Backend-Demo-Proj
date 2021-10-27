import json
from json import dumps, loads
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
import datetime

# Create your views here.


def home(request):
    template_name="index/index.html"
    context = {
        
    }
    return render(request,template_name,context)