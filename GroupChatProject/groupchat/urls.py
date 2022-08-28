from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.chats, name='chats'),
    path('<slug:slug>/', views.startChat, name='chat'),
]