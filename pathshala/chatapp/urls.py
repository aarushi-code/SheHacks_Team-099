from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    
    path('', login_required(views.index), name='index'),
    path('<str:room_name>/', views.room, name='room'),
    path('search/', views.search, name='search'),
]
