from django.shortcuts import render, get_object_or_404

def index(request):
    template_name="index/index.html"
    context = {}
    return render(request,template_name,context)
