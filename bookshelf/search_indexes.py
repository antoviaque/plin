
# Imports #####################################################################

from haystack import indexes

from .models import Book


# Classes #####################################################################

class BookIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    subtitle = indexes.CharField(model_attr='subtitle', null=True)
    isbn = indexes.CharField(model_attr='isbn')
    author = indexes.CharField(model_attr='author')
    illustrator = indexes.CharField(model_attr='illustrator', null=True)
    editor = indexes.CharField(model_attr='editor')
    collection = indexes.CharField(model_attr='collection', null=True)
    keywords = indexes.CharField(model_attr='keywords', null=True)
    synopsis = indexes.CharField(model_attr='synopsis')

    def get_model(self):
        return Book
