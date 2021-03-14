from django.contrib import admin
from django.urls import path,include
from msat import views
from django.contrib.auth import views as auth_views
#from login import views as v

urlpatterns = [
    
    path('test/', views.home, name='test'),
]