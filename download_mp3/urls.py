from django.urls import path
from download_mp3 import views

urlpatterns = [
    path('', views.descarga, name="descarga")
]
