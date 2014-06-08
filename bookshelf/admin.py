
# Imports #########################################################################################

from django import forms
from django.contrib import admin

from admintimestamps import TimestampedAdminMixin
from selectable.forms import widgets

from .lookups import KeywordLookup
from .models import Author, Book, Collection, Editor, Keyword, ReaderLevel, Review
from .reviews import ReviewAdmin


# Main ############################################################################################

class TimestampedAdmin(TimestampedAdminMixin, admin.ModelAdmin):
    pass


class BookAdminForm(forms.ModelForm):
    class Meta(object):
        model = Book
        widgets = {
            'keywords': widgets.AutoCompleteSelectMultipleWidget(lookup_class=KeywordLookup),
        }


class BookAdmin(TimestampedAdmin):
    form = BookAdminForm

admin.site.register(Author, TimestampedAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Collection, TimestampedAdmin)
admin.site.register(Editor, TimestampedAdmin)
admin.site.register(Keyword, TimestampedAdmin)
admin.site.register(ReaderLevel, TimestampedAdmin)
admin.site.register(Review, ReviewAdmin)

