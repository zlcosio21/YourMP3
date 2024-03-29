from django.http import FileResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from pytube import YouTube
import os

# Create your views here.
def descarga(request):
    if request.method == "POST":
        url = request.POST.get("url")

        try:
            video_url = YouTube(url)
            audio = video_url.streams.filter(only_audio=True).first()
        except:
            messages.error(request, "La url es incorrecta, por favor ingrese una nuevamente")
            return redirect("descarga")

        video_url = YouTube(url)

        audio = video_url.streams.filter(only_audio=True).first()
        audio_name = audio.download()

        convert_mp3 = os.path.splitext(audio_name)[0] + ".mp3"
        os.rename(audio_name, convert_mp3)

        response = FileResponse(open(convert_mp3, "rb"))
        response["Content-Disposition"] = f'attachment; filename="{os.path.basename(convert_mp3)}"'

        return response

    return render(request, "download_mp3/descarga.html")
