from django.urls import include, path
from . import views

urlpatterns = [
    # This URL is equivalent to the user typing /music/ in the search bar.
    path('', views.index, name='index'),
    path('<int:album_id>/', views.details, name='details')
]
