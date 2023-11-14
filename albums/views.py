from django.shortcuts import render, get_object_or_404, redirect
from .forms import AlbumForm
from .models import Album


# Create your views here.
def home(request):
    album = Album.objects.all()
    return render(request, 'albums/index.html', {'album': album})


def album_details(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, 'album_detail.html', {'album': album})


def create_album(request, album_pk):
    album = get_object_or_404(Album, pk=album_pk)
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        new_album = form.save(commit=False)
        new_album.album = album
        new_album.save()
        return redirect('home')
    form = AlbumForm()
    return render(request, 'create_album.html', {'form': form})