"""blog_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
# https://docs.djangoproject.com/en/3.1/topics/auth/default/
from django.contrib.auth import views as auth_views
from django.urls import path, include
# https://docs.djangoproject.com/en/3.1/howto/static-files/
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from .views import index
from accounts import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index,name="index"),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='apps/accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='apps/accounts/logout.html'), name='logout'),
    path('blog/', include('blog.urls')),
    path('cfeblog/', include('cfeblog.urls',namespace="cfeblog")),
]

# https://docs.djangoproject.com/en/3.1/howto/static-files/
# the settings are not usable during production so that is why they debug settings is when this works
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)