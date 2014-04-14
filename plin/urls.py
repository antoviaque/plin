
# Imports #########################################################################################

from django.conf.urls import patterns, include, url
from django.contrib import admin


# Admin ###########################################################################################

admin.autodiscover()


# URLs ############################################################################################

urlpatterns = patterns('',
    url(r'^$', 'bookshelf.views.book_search', name='home'),
    url(r'^bookshelf/', include('bookshelf.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
