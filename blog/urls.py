"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path ,include
from blogapp.views import home , contact, article, signup, blogpost ,login ,logout, search, addarticles


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('contact', contact, name="contact"),
    path('article', article, name="article"),
    path('blog/<int:pk>', blogpost , name='blogpost'),
    path('signup', signup, name="signup"),
    path('login', login, name="login"),
    path('logout', logout, name="logout"),
    path('search', search, name="search"),
    path('addarticles', addarticles, name="addarticles"),
]
