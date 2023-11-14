from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('albums/<int:pk>', views.AlbumDetailsView.as_view(), name='album_details'),
    path('albums/<int:album_pk>/album/new', views.create_album, name='create-album'),
]

