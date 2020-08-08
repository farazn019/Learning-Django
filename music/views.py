from django.http import HttpResponse
from django.shortcuts import render
from .models import Album

# Create your views here.


def index(request):
    all_albums = Album.objects.all()
    context = {'all_albums':  all_albums}
    return render(request, 'templates/music/index.html')


def details(request, album_id):
    return HttpResponse("<h3>The list:</h3>")


