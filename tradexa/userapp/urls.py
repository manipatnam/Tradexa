from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [path("", views.postforms2),
    #path('', views.postforms, name='test'),
    path('login', views.login, name='login'),
path('logout', views.logout, name='logout')
]
