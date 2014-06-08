
# Imports #########################################################################################

import pyisbn

from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied, ValidationError
from django.db import models
from django_extensions.db.models import TimeStampedModel
from django_languages.fields import LanguageField

from autoslug import AutoSlugField
from djangoratings.fields import RatingField
from south.modelsinspector import add_introspection_rules

from .htmlcleaner import cleaner


# South ###########################################################################################

add_introspection_rules([], ["^django_languages\.fields\.LanguageField"])


# Validators ######################################################################################

def validate_isbn(isbn):
    if not pyisbn.validate(isbn):
        raise ValidationError(u'{} is not a valid ISBN number'.format(isbn))


# Classes #########################################################################################

class Author(TimeStampedModel):
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name


class Collection(TimeStampedModel):
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name


class Editor(TimeStampedModel):
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name


class ReaderLevel(TimeStampedModel):
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name


class Keyword(TimeStampedModel):
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name


class Review(TimeStampedModel):
    book = models.ForeignKey('Book')
    user = models.ForeignKey(User)
    content = models.TextField()

    class Meta:
        unique_together = ('book', 'user')

    def __unicode__(self):
        return u'{}: "{}"'.format(self.user, self.content)

    def save(self, *args, **kwargs):
        # Ensure user-submitted HTML content is always safe
        self.content = cleaner.clean_html(self.content)
        super(Review, self).save(*args, **kwargs)


class Book(TimeStampedModel):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title')
    subtitle = models.CharField(max_length=200, blank=True)
    isbn = models.CharField(max_length=13, unique=True, validators=[validate_isbn])
    author = models.ForeignKey(Author)
    illustrator = models.ForeignKey(Author, null=True, blank=True, related_name='book_illustrator_set')
    editor = models.ForeignKey(Editor)
    collection = models.ManyToManyField(Collection)
    language = LanguageField()
    pub_year = models.IntegerField('year published')
    reader_level = models.ForeignKey(ReaderLevel)
    nb_pages = models.IntegerField()
    cover = models.ImageField(upload_to='covers')
    keywords = models.ManyToManyField(Keyword)
    synopsis = models.TextField()
    rating = RatingField(range=5, can_change_vote=True)

    def __unicode__(self):
        return self.title

    @property
    def isbn_10(self):
        if len(self.isbn) == 10:
            return self.isbn
        else:
            return pyisbn.convert(self.isbn)

    @property
    def overall_rating(self):
        """
        Returns the cumulated public rating of the book
        """
        return self.rating.get_rating()

    def get_user_rating(self, request):
        """
        The rating the request user gave for a given book
        """
        if request.user.is_authenticated():
            rating = self.rating.get_rating_for_user(request.user, request.META['REMOTE_ADDR'])
        else:
            rating = None
        return rating

    def set_user_rating(self, request, rating):
        """
        Set rating for a given user on the current book, using request context for auth/antispam
        """
        if not request.user.is_authenticated():
            raise PermissionDenied

        self.rating.add(score=rating, user=request.user, ip_address=request.META['REMOTE_ADDR'])
