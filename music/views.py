from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("<script>console.log('Hello and welcome to the music page')</script>")

def details(request, album_id):
    return HttpResponse("<h3>The list:</h3>")


