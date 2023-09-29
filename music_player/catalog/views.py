from django.shortcuts import render
from django.contrib.auth.hashers import make_password, check_password
from catalog.models import User
from django.db import IntegrityError, transaction
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm
from catalog.models import Song
from django.db.models import Count
from django.db.models import F
from django.shortcuts import get_object_or_404
# Create your views here.


def index(request):
    return render(request, 'homepage/song_card.html', {})

def songs(request):
    song = Song.objects.all().order_by('-name')
    # dd(song)
    return render(request, 'song_page/song_page.html', {'song': song})
# {'song': song}: can co cai nay, o day de tra bien song ve 'song_page/song_page.html' duoi dang object ten la 'song'. Cai o trong '' la ten bien ma o muon tra n ve, cai sau dau : la bien o muon tra ve

def songpost(request, id):
    song = Song.objects.get(pk = id)
    song.listen_count = F('listen_count') + 1
    song.save()
    return render(request, 'song_page/songpost.html', {'song': song})


def search(request):
    query = request.GET.get("query")
    qs = Song.objects.filter(name__icontains=query)
    return render(request, 'song_page/search.html', {"songs": qs})

def trending(request):
    trending = Song.objects.all().order_by('-listen_count')
    return render(request, 'song_page/trending.html', {'trending': trending})

def song_card_partial(request):
    return render(request, 'homepage/song_card.html', {})
