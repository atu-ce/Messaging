"""src URL Configuration

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
from django.urls import path


from django.contrib.auth import views as auth_views

from app.views import anasayfa, home, profile, about, article_detail

    

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html')),
    path('logout/', auth_views.LogoutView.as_view()),

    path('',home),#Burda giriş yapılana kadar kalıcak olan anasayfaya gidicek. 
    path('home/',anasayfa),#Bura giriş yapıldığında oluşucak olan anasayfaya gidicek.

    path('profile/',profile),
    path('profile/<int:id>', article_detail),

    path('about',about),

]
