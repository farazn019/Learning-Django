from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', admin.site.urls), #Remember to change this later to an actual home-page.
    path('admin/', admin.site.urls),
    path('music/', include('music.urls'))
]
