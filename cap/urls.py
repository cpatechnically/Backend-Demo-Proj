"""cap URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

from accounts.views import (
    login_view,
    logout_view,
    register_view,
    AccountHomeView
)

from .views import home
template_path = 'reactdj/home.html'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name="index"),
    path('login/', login_view,name="login"),
    path('logout/', logout_view,name="logout"),
    path('register/', register_view),
    path('captures/', include('captures.urls',namespace="captures")),
    path('posts/', include('posts.urls',namespace="posts")),
    path('cfereact/', include('cfereact.urls',namespace="cfereact")),
    path('search/', include('search.urls',namespace="search")),
    path('demo/', include('demo.urls',namespace="demo")),
    path('accounts/', AccountHomeView.as_view(), name="accthome"),
    path('tweetme/', include('tweetme.urls',namespace="tweetme")),
    path('survey/', include('survey.urls',namespace="survey")),
    path('vidly/', include('vidly.urls',namespace="vidly")),
    path('htmlcss/', include('htmlcss.urls',namespace="htmlcss")),
    #path('localconfig/', include('shaferdj.urls',namespace="shaferdj")),
    path('shaferdj/', include('shaferdj.urls',namespace="shaferdj")),
    path('react/',TemplateView.as_view(template_name='reactdj/npx_home.html'),name='react'),

    path("api/vidly/",include("vidly.api.urls")),
    path("api/captures/",include("captures.api.urls")),
    path("api/posts/",include("posts.api.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
