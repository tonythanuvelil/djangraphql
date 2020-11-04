from django.db import models
from ..genres.models import Genre
from ..authors.models import Author


class Book(models.Model):
    name = models.CharField(max_length=200)
    genre = models.ForeignKey(Genre, on_delete=models.DO_NOTHING)
    author = models.ForeignKey(
        Author, related_name="books", on_delete=models.DO_NOTHING)
    year = models.IntegerField()

    def __str__(self):
        return self.name
