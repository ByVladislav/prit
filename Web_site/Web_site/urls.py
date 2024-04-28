"""
URL configuration for Web_site project.

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
from django.contrib import admin
from django.urls import path
from web import views
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', views.admin),
    path('account/my/new/', views.new),
    path('account/my/', views.acc),
    path('', views.about),
    path('info/<str:title>/<str:text>/', views.info),
    path('main/', views.index),
    path('pet/', views.pet),
    path('pet/<int:num>/', views.pet),
    path('pet/next/<int:num>/', views.Pnext),
    path('pet/back/<int:num>/', views.Pback),
    path('pet/wish/<int:num>/', views.Pwish),
    path('pet/forum/<int:num>/', views.Pforum),
    path('pet/take/<int:num>/', views.Ptake),
    path('report/', views.report),
    path('report/pet/', views.RPpet),
    path('account/', views.account),
    path('account/exit/', views.ext),
    path('account/registration/login/', views.Rlogin),
    path('account/login/', views.login),
    path('account/registration/', views.reg)
]

