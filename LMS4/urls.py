"""LMS3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
#from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('LMS4app.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('', TemplateView.as_view(template_name='choice.html')), 
    # path('adduser.html/', TemplateView.as_view(template_name='adduser.html')),
    # path('createbook.html/', TemplateView.as_view(template_name='createbook.html')),
    # path('updatebook.html/', TemplateView.as_view(template_name='updatebook.html')),
    # path('deletebook.html/', TemplateView.as_view(template_name='deletebook.html')),
    # path('allbooks.html/', TemplateView.as_view(template_name='allbooks.html')) ,
]

