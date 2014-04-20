
# Imports #########################################################################################

from django.db import models
from django_extensions.db.models import TimeStampedModel


# Classes #########################################################################################

class Author(TimeStampedModel):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Collection(TimeStampedModel):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Editor(TimeStampedModel):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class ReaderLevel(TimeStampedModel):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Book(TimeStampedModel):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, blank=True)
    author = models.ForeignKey(Author)
    illustrator = models.ForeignKey(Author, null=True, blank=True, related_name='book_illustrator_set')
    editor = models.ForeignKey(Editor)
    collection = models.ForeignKey(Collection, null=True, blank=True)
    pub_date = models.DateTimeField('date published')
    reader_level = models.ForeignKey(ReaderLevel)
    nb_pages = models.IntegerField()
    synopsis = models.TextField()

    # TODO: use plugins for these fields
    #cover = models.ImageField()
    #keywords = models.CharField(max_length=200)
    #language = models.CharField(max_length=2)
    #isbn = models.CharField(max_length=20)

    #votes = models.IntegerField(default=0)
    #comments = models.CharField(max_length=200)

    def __unicode__(self):
        return self.title

