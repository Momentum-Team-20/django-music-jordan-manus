# Generated by Django 4.2.7 on 2023-11-14 15:35

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Album",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("album_name", models.CharField(blank=True, max_length=500)),
                ("num_of_tracks", models.IntegerField(blank=True, null=True)),
                ("release_date", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
