"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
#using a variable name in case i import another view on accident
from register.views import register as r
from home.views import home_view as h
from django.contrib.auth import views as auth_views
from main.views import main_page as main
from register.views import login_view as l

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
urlpatterns = [
    path('',h ,name="home"),
    path('admin/', admin.site.urls),
    path("register/", r, name="register"),
    path('login/',l,name = 'login'),
    path('main/',main, name="hidden"),
    #path('hidden/', l, name="hidden")
]
