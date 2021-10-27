from django.shortcuts import render

# Create your views here.

def react_spa(request):
    template_name="apps/survey/react_spa.html"

    context={
        "pgname":"Survey"
    }
    return render(request,template_name,context)