from django.shortcuts import render


def react_spa(request):
    template_name="apps/posts/react_spa.html"

    context={
        "pgname":"Posts"
    }
    return render(request,template_name,context)