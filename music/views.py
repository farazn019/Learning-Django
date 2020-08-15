from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Album

# Create your views here.


def index(request):
    all_albums = Album.objects.all()
    template = loader.get_template('music/index.html')
    context = {'all_albums': all_albums}
    return HttpResponse(template.render(context, request))


def details(request, album_id):
    return HttpResponse("<h3>The list:</h3>")


