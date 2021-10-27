from django.shortcuts import render

# Create your views here.
def react_spa(request):
    template_name="apps/cfereact/react_spa.html"

    context={
        "pgname":"Posts"
    }
    return render(request,template_name,context)