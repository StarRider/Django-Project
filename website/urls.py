# -*- coding: utf-8 -*-
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name = "WhiteFlames-Home"),
    path('about/', views.about, name = "WhiteFlames-About"),
    path('nextPage/', views.nextPage, name = "WhiteFlames-nextPage"),
    path('prevPage/', views.prevPage, name = "WhiteFlames-prevPage")
]

