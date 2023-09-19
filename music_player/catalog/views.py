from django.shortcuts import render
from django.contrib.auth.hashers import make_password, check_password
from catalog.models import User
from django.db import IntegrityError, transaction
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.


def index(request):
    return render(request, 'homepage/song_card.html', {})


def register_user(request):
    if (request.POST.get("password1") != request.POST.get("password1")):
        # return render(request, 'registration/login.html', {'error': "Password didn't match!"})
        raise Exception("Password didn't match!")
    try:
        user = User.objects.get_or_create(
            username=request.POST.get("username"),
            email=request.POST.get("email"),
            password=make_password(request.POST.get("password1")),
        )
        return render(request, 'registration/login.html', {})
    except IntegrityError as e:
        # return render(request, 'registration/login.html', {'error': "Username or email has been used!"})
        raise e
