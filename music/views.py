from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("<script>alert('Hello and welcome to the music page')</script>")