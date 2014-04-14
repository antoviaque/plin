
# Imports #########################################################################################

from django.db import models
from django_extensions.db.models import TimeStampedModel


# Classes #########################################################################################

class Author(TimeStampedModel):
    name = models.CharField(max_length=200)


class Collection(TimeStampedModel):
    name = models.CharField(max_length=200)


class Editor(TimeStampedModel):
    name = models.CharField(max_length=200)


class ReaderLevel(TimeStampedModel):
    name = models.CharField(max_length=200)


class Book(TimeStampedModel):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, blank=True)
    author = models.ForeignKey(Author)
    illustrator = models.ForeignKey(Author, null=True, related_name='book_illustrator_set')
    collection = models.ForeignKey(Collection, null=True)
    pub_date = models.DateTimeField('date published')
    reader_level = models.ForeignKey(ReaderLevel)
    nb_pages = models.IntegerField()
    synopsis = models.TextField()

    # TODO: use plugins for these fields
    #votes = models.IntegerField(default=0)
    #keywords = models.CharField(max_length=200)
    #comments = models.CharField(max_length=200)
    #language = models.CharField(max_length=2)
    #isbn = models.CharField(max_length=20)
    #cover = models.ImageField()


