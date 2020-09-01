from django.urls import include, path, re_path
from . import views

urlpatterns = [
    # This URL is equivalent to the user typing /music/ in the search bar.
    re_path(r'^$', views.index, name='index'),
    path('<int:album_id>/', views.details, name='details')
]
