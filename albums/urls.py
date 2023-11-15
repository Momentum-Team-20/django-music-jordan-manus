from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('new/', views.create_album, name='post_album'),
    path('albums/<int:pk>', views.AlbumDetailsView.as_view(), name='album_details'),
    path('albums/<int:album_pk>/edit', views.edit_album, name='edit-album'),
    path('albums/<int:pk>/delete', views.delete_album, name='delete-album'),
]

