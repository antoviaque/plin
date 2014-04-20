
# Imports #########################################################################################

from django.contrib import admin
from bookshelf.models import Author, Book, Collection, Editor, Keyword, ReaderLevel
from admintimestamps import TimestampedAdminMixin


# Main ############################################################################################

class TimestampedAdmin(TimestampedAdminMixin, admin.ModelAdmin):
    pass

admin.site.register(Author, TimestampedAdmin)
admin.site.register(Book, TimestampedAdmin)
admin.site.register(Collection, TimestampedAdmin)
admin.site.register(Editor, TimestampedAdmin)
admin.site.register(Keyword, TimestampedAdmin)
admin.site.register(ReaderLevel, TimestampedAdmin)

