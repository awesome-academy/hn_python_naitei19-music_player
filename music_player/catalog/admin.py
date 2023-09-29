from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .models import Song
from .models import Tag

class SongTagInline(admin.TabularInline):
    model = Song.tags.through

class SongAdmin(admin.ModelAdmin):
    inlines = [SongTagInline]

admin.site.register(User, UserAdmin)
admin.site.register(Song, SongAdmin)
admin.site.register(Tag)
