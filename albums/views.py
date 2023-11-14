from django.shortcuts import render
from .models import Album


# Create your views here.
def list_albums(request):
    album = Album.objects.all()
    return render(request, 'albums/index.html', {'album': album})
