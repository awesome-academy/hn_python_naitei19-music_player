from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .models import Song , Playlist , UserSong , Listenlater, Comment , Report
from .models import Tag

class SongTagInline(admin.TabularInline):
    model = Song.tags.through

class SongAdmin(admin.ModelAdmin):
    inlines = [SongTagInline]

admin.site.register(User, UserAdmin)
admin.site.register(Song, SongAdmin)
admin.site.register(Playlist)
admin.site.register(UserSong)
admin.site.register(Listenlater)
admin.site.register(Comment)
admin.site.register(Report)
admin.site.register(Tag)






