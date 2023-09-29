from django.shortcuts import render
from django.contrib.auth.hashers import make_password, check_password
from catalog.models import User
from django.db import IntegrityError, transaction
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.


def index(request):
    return render(request, 'homepage/song_card.html', {})
