from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('songs/', views.songs, name='songs'),
    path('songs/<int:id>', views.songpost, name='songpost'),
    path('search/', views.search, name='search'),
    path('playlist/',views.playlist,name='playlist'),
    path('usersong/',views.usersong,name='usersong'),
    path('listenlater/',views.listenlater,name='listenlater'),
    path('upload/',views.upload,name='upload'),
    path('creatplaylist/',views.creatplaylist,name='creatplaylist'),
    path('addplaylist/',views.addtoplaylist,name='addplaylist'),
    path('playlists/<int:id>',views.playlistdisplay, name='playlistdetails'),
    path('trending/', views.trending, name='trending'),
    # path('songs/<int:id>/', views.song_detail, name='song_detail'),
    path('report/', views.report_song, name='report_song'),
]


