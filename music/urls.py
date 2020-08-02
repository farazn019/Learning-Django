from django.conf.urls import url
from . import views

urlpatterns = [
    url('', views.index, name="index")    #If the user just types the website name, then it will take the user to the home page (index).

]