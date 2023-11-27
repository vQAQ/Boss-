from django.urls import path, re_path
from myApp import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('registry/', views.registry, name='registry'),
    path('home/', views.home, name='home')
]
