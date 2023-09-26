from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .models import Song , Playlist , UserSong , Listenlater

admin.site.register(User, UserAdmin)
admin.site.register(Song)
admin.site.register(Playlist)
admin.site.register(UserSong)
admin.site.register(Listenlater)

