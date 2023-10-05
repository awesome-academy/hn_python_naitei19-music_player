from django.shortcuts import render
from catalog.models import Song,Listenlater ,UserSong,Playlist, Comment ,Report, User
from django.shortcuts import redirect
from django.utils.html import escape
from django.http import HttpResponse
from django.db.models import Count
from django.db.models import F 
from django.shortcuts import get_object_or_404
from django.contrib import messages
from .forms import reportForm
from django.db.models import Q
from django.db import connection, transaction




def usersong(request):
    """to record a listen history and return the user's history"""
    if request.method == "POST" :
        # dd(request)
        song_id = request.POST['song']
        user = request.user
        song = Song.objects.filter(id = song_id).first()
        # dd(song)
        usersong = UserSong(user = user , song = song )
        usersong.save()
        return redirect(f"/catalog/songs/{song_id}")
    history = UserSong.objects.filter(user = request.user)
    # dd(history)
    return render(request,'catalog/usersong.html',{"history":history})

def listenlater(request):
    if request.method == "POST" :
        # dd(request)
        listen_id = request.POST['listen_id']
        addll = Song.objects.filter(id = request.POST['listen_id']).first()
        user = request.user
        listen = Listenlater.objects.filter(user=user)
        for i in listen:
            if addll == i.listen:
                break
        else:
            listenlater = Listenlater(user = user , listen = addll)
            listenlater.save()
        
        return redirect(f"/catalog/songs/{listen_id}")
        
    
    ll = Listenlater.objects.filter(user = request.user)

    return render(request,'catalog/listenlater.html',{"song":ll})
    
def playlistdisplay(request, id):
    playlist_id = id
    playlist = Playlist.objects.filter(id = playlist_id).first()
    # songs = playlist.songs.all()
    # dd(songs)
    # dd(playlist)
    return render(request, 'catalog/playlist_details.html', {'playlist':playlist})

def playlist(request):
    playlist = Playlist.objects.all()
    return render(request,'catalog/playlist.html', {'playlist': playlist})

def creatplaylist(request):
    name = ""
    owner = ""
    image = None

    if request.method == "POST":
        # dd(request)
        name = request.POST.get('name')  
        current_user = request.user
        owner = current_user
        image = request.FILES['image']  
        
        if name and owner:  
            
            song_model = Playlist(name=name, owner=owner, image=image)
            song_model.save()
            return redirect(f"/catalog/creatplaylist/")  

    return render(request, "catalog/creatplaylist.html")

def index(request):
    song = Song.objects.all()
    return render(request, 'homepage/song_card.html', {'song': song})

def songs(request):
    song = Song.objects.all()
    playlist = Playlist.objects.filter(owner = request.user)
    return render(request, 'song_page/song_page.html', {'song': song, 'playlists': playlist})
# {'song': song}: can co cai nay, o day de tra bien song ve 'song_page/song_page.html' duoi dang object ten la 'song'. Cai o trong '' la ten bien ma o muon tra n ve, cai sau dau : la bien o muon tra ve

def songpost(request, id):
    song = Song.objects.get(pk = id)
    comments = Comment.objects.filter(song = song).all()
    song.listen_count = F('listen_count') + 1
    song.save()
    recommended = Song.objects.filter(Q(artist = song.artist)|Q(tags__in=song.tags.all())).exclude(id=song.id).distinct()
    like_count = UserSong.objects.filter(song = song, like = True).count()
    if request.method == 'POST':
            # dd(request)
            user = request.user
            text = request.POST['text']
            # dd(request)
            saveComment = Comment(user = user, song = song, text = text)
            saveComment.save()
            return redirect(f"/catalog/songs/{id}")
    return render(request, 'song_page/songpost.html', {'song': song, 'comments': comments, 'recommended_song': recommended, 'like_count': like_count})

def search(request):
    query = request.GET.get("query")
    qs = Song.objects.filter(name__icontains=query)
    return render(request, 'song_page/search.html', {"songs": qs})

# def upload(request):
#     if request.method == "POST":
#         name = request.POST['name']
#         artist = request.POST['artist']
#         image = request.FILES['file']
#         content = request.FILES['file']
    
#     song_model = Song(name=name ,artist=artist)
#     song_model.save()

#     return render(request,"catalog/upload.html")

def upload(request):
    name = ""
    artist = ""
    image = None
    content = None
    # rq = request
    print(request)
    if request.method == "POST":
        name = request.POST.get('name')  
        current_user = request.user
        artist = current_user
        image = request.FILES['image']  
        content = request.FILES['content'] 
        if name and artist :  
            
            song_model = Song.objects.create(name=name, artist=artist, image=image, content=content)
            song_model.save()
            
            return redirect(f"/catalog/upload/")  

    return render(request, "catalog/upload.html")
    
def addtoplaylist(request):
    if request.method == "POST":
        # dd(request)
        song_id = request.POST['song_id']
        playlist_id = request.POST['playlist_id']
        song = Song.objects.filter(id = song_id).first()
        playlist = Playlist.objects.filter(id = playlist_id).first()
        playlist.songs.add(song)
        return redirect(f"/catalog/songs/")

def trending(request):
    trending = Song.objects.all().order_by('-listen_count')
    return render(request, 'catalog/trending.html', {'trending': trending})

def song_detail(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    comments = song.comments.all()
    user = request.user
    text = request.post['text']
    if request.method == 'POST':
            saveComment = Comment(user = user, song = song, text = text)
            saveComment.save()
            return redirect(f"/catalog/songs/{song_id}")
    


    return render(request, 'catalog/song_detail.html', {'song': song, 'comments': comments})

def report_song(request):
    song_id = request.POST['song_id']
    song = get_object_or_404(Song, pk=song_id)
    if request.method == 'POST':
        form = reportForm(request.POST)
        if form.is_valid():
            reason = form.cleaned_data['reason']
            report = Report(song=song, reason=reason)
            report.save()
            return redirect(f"/catalog/songs/{song_id}")
    else:
        form = reportForm()

    return render(request, 'catalog/report_song.html', {'form': form})

def artist(request, artist_id):
    user = User.objects.get(pk = artist_id)
    # dd(user)
    song = Song.objects.filter(artist = user).all()
    # dd(song)
    recommended1 = Song.objects.filter(artist_id=artist_id).order_by('-name')
    #dd(recommended1)
    return render(request, 'song_page/artist.html', {'song': song, 'recommended1_song': recommended1,'artist':user})

def song_card_partial(request):
    return render(request, 'homepage/song_card.html', {})

def recommended_song(request, id):
    song = Song.objects.get(pk = id)
    recommended = Song.objects.filter(Q(artist = song.artist)|Q(tags__in=song.tags.all())).exclude(id=song.id).distinct()
    return render(request, 'song_page/recommended_song.html', {'song': song, 'recommended': recommended})

def like_song(request):
    song_id = request.POST['listen_id']
    user = request.user
    song = Song.objects.filter(pk = song_id).first()
    comments = Comment.objects.filter(song = song).all()
    recommended = Song.objects.filter(Q(artist = song.artist)|Q(tags__in=song.tags.all())).exclude(id=song.id).distinct()
    # dd(song)
    like_song = UserSong(song = song, user = user)
    like_song.save()
    like = UserSong.objects.filter(song = song, user = user).first()
    # dd(like)
    if (like.like == False):
        like.like = True
    else:
        like.like = False
    like.save()    
    like_count = UserSong.objects.filter(song = song, like = True).count()
    song.like_count = like_count
    song.save()
    # dd(like_count)
    # dd(1)   
    return render(request, 'song_page/songpost.html', {'song': song, 'comments': comments, 'recommended_song': recommended, 'like_count': like_count})

def display_most_like(request):
    song = Song.objects.all().order_by('-like_count')
    return render(request, 'song_page/display_most_like.html', {'display_most_like': song})