from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .forms import AlbumForm
from .models import Album


# creates the home page with list of albums
def home(request):
    albums = Album.objects.all()
    return render(request, 'albums/index.html', {'albums': albums})


# creates a new album with a form
def create_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        new_album = form.save(commit=False)
        new_album.save()
        return redirect('home')
    form = AlbumForm()
    return render(request, 'albums/post_album.html', {'form': form})


# displays album details
class AlbumDetailsView(generic.DetailView):
    model = Album
    template_name = 'albums/album_details.html'


# updates album details by reusing the original form data
def edit_album(request, album_pk):
    album = get_object_or_404(Album, pk=album_pk)
    # album = Album.objects.get(pk=album_pk)

    if request.method == 'GET':
        context = {'form': AlbumForm(instance=album), 'pk': album_pk}
        return render(request, 'albums/post_album.html', context)
    
    elif request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            messages.success(request, 'The post has been updated successfully.')
            return redirect('home')
        else:
            return render(request, 'albums/post_form.html', {'form': form})


# deletes album from list of albums
def delete_album(request, album_pk):
    album = get_object_or_404(Album, pk=album_pk)
    # album = Album.objects.get(pk=album_pk)
    context = {'album': album}

    if request.method == 'GET':
        return render(request, 'albums/delete_album.html', context)
    elif request.method == 'POST':
        album.delete()
        return redirect('home')