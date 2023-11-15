from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .forms import AlbumForm
from .models import Album


# Create your views here.
def home(request):
    albums = Album.objects.all()
    return render(request, 'albums/index.html', {'albums': albums})


def create_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        new_album = form.save(commit=False)
        new_album.save()
        return redirect('home')
    form = AlbumForm()
    return render(request, 'albums/post_album.html', {'form': form})


class AlbumDetailsView(generic.DetailView):
    model = Album
    template_name = 'albums/album_details.html'


def edit_album(request, album_pk):
    post = get_object_or_404(Album, pk=album_pk)

    if request.method == 'GET':
        context = {'form': AlbumForm(instance=post), 'pk': album_pk}
        return render(request, 'albums/post_album.html', context)
    elif request.method == 'POST':
        form = AlbumForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'The post has been updated successfully.')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the follwoing errors: ')
            return render(request, 'albums/post_form.html', {'form': form})


def delete_album(request, album_pk):
    pass