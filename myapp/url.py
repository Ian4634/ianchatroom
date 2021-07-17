from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home',),
    path('create/', views.create, name = 'test1'),
    path('<str:room>/<str:username>/', views.room, name = 'room'),
    path('<str:room>/<str:username>/send/', views.send,name = 'send')
]