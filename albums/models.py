from django.db import models


# Create your models here.
class Album(models.Model):
    album_name = models.CharField(max_length=500, blank=True)
    artist = models.CharField(max_length=150, blank=True)
    num_of_tracks = models.IntegerField(null=True, blank=True)
    release_date = models.DateField()

    def __str__(self) -> str:
        return f'{self.album_name}'
    