"""
URL configuration for gameapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
   path('',views.home,name="home"),
#    path('about/', views.about, name="about.html"),
# path('passvalue/', views.passvalue, name="passvalue.html"),
# path('passvalue/add/', views.addition, name="addition.html"),
#
#    path('contact/', views.contact, name="contact"),
#    path('detail/', views.detail, name="detail.html"),
#    path('thanks/', views.thanks, name="thanks")

]
