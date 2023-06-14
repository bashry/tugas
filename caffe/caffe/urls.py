from django.contrib import admin
from django.urls import path
from daftar.views import daftar, tempat


urlpatterns = [
    path('admin/', admin.site.urls),
    path('daftar/', daftar),
    path('tempat/', tempat),
    
]

