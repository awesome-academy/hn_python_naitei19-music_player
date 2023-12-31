from telnetlib import STATUS
from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import AbstractUser
from django.forms import ModelForm
from django.forms import forms
from django.conf import settings
# from . import Tag, Song
# Create your models here.
# class User(AbstractUser):
#     pass

class Tag(models.Model):
    """model representing a song tags"""
    name = models.CharField(
        max_length=20, help_text=_('Enter a song tags'))

    def __str__(self):
        """String for representing the Model object"""
        return self.name

class Song(models.Model):
    """Model representing a song"""
    name = models.CharField(
        max_length=200, help_text=_('Enter a song name'))
    image = models.ImageField(
        upload_to='cover_image')
    content = models.FileField(upload_to='songs')
    artist = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Use the AUTH_USER_MODEL setting
        on_delete=models.CASCADE,
        null=True
    )
    status = models.BooleanField(
        default=False,
        help_text=_('Check this box to make the song public')
    )
    listen_count = models.PositiveIntegerField(default=0)
    like_count = models.PositiveBigIntegerField(default=0)
    tags = models.ManyToManyField(Tag, through='SongTag',through_fields=('song','tag'))

    def display_tags(self):
        return ', '.join(tag.name for tag in self.tags.all()[:3])
    
    display_tags.short_description = 'Tags'

    def __str__(self):
        """Return song name"""
        return self.name

    class Meta:
        ordering = ["name"]

class SongTag(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)

class User(AbstractUser):
    history = models.ManyToManyField(Song, through='UserSong', through_fields=('user','song'))

class Playlist(models.Model):
    name = models.CharField(
        max_length=200, help_text=_('Enter a playlist name'))
    image = models.ImageField(upload_to='cover_image',
                              height_field='', width_field='')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    songs = models.ManyToManyField(Song, through='PlaylistSong',through_fields=('playlist','song'))

    def __str__(self):
        """Return playlist name"""
        return self.name

    class Meta:
        ordering = ["name"]

class PlaylistSong(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)

class UserSong(models.Model): 
    # his_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    like = models.BooleanField(default = False)

    
    
class Listenlater(models.Model): #Listen later
    #listen = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listen= models.ForeignKey(Song, on_delete=models.CASCADE)


class Comment(models.Model):
    text = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)  # Change 'article' to 'song'
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.song.name}"
    
class Report(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    reason = models.TextField()

    def __str__(self):
        return f"Report for {self.song.name}"
    
        