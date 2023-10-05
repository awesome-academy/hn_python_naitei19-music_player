from telnetlib import STATUS
from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Tag(models.Model):
    """model representing a song tags"""
    name = models.CharField(
        max_length=20, help_text=_('Enter a song tags'))

    def __str__(self):
        """String for representing the Model object"""
        return self.name


class User(AbstractUser):
    email = models.EmailField(unique=True)


class Song(models.Model):
    """Model representing a song"""
    name = models.CharField(
        max_length=200, help_text=_('Enter a song name'))
    image = models.ImageField(upload_to='cover_image')
    content = models.FileField(upload_to='songs')
    artist = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(
        default=False,
        help_text=_('Check this box to make the song public')
    )
    listen_count = models.PositiveIntegerField(default=0)
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

class Playlist(models.Model):
    name = models.CharField(
        max_length=200, help_text=_('Enter a playlist name'))
    image = models.ImageField(upload_to='cover_image',
                              height_field=100, width_field=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return playlist name"""
        return self.name

    class Meta:
        ordering = ["name"]
