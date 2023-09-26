from telnetlib import STATUS
from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.


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
        max_length=200, help_text=_('Enter a song name'), default = '')
    image = models.ImageField(
        upload_to='cover_image')
    content = models.FileField(upload_to='songs')
    artist = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Use the AUTH_USER_MODEL setting
        on_delete=models.SET_NULL,
        null=True
    )
    status = models.BooleanField(
        default=False,
        help_text=_('Check this box to make the song public')
    )

    def __str__(self):
        """Return song name"""
        return self.name

    class Meta:
        ordering = ["name"]

class User(AbstractUser):
    email = models.EmailField(unique=True)
    history = models.ManyToManyField(Song, through='UserSong', through_fields=('user','song'))

class Playlist(models.Model):
    name = models.CharField(
        max_length=200, help_text=_('Enter a playlist name'), default = '')
    image = models.ImageField(upload_to='cover_image',
                              height_field=100, width_field=100)
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

    
class Listenlater(models.Model): #Listen later
    #listen = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listen= models.ForeignKey(Song, on_delete=models.CASCADE)

class Download(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=0)