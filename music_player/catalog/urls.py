from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('songs/', views.songs, name='songs'),
    path('songs/<int:id>', views.songpost, name='songpost'),
    path('search/', views.search, name='search'),
    path('trending/', views.trending, name='trending'),
]
