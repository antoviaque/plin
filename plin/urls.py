
# Imports #########################################################################################

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin


# Admin ###########################################################################################

admin.autodiscover()


# URLs ############################################################################################

urlpatterns = patterns('',
    url(r'^$', 'bookshelf.views.index', name='home'),
    url(r'^bookshelf/', include('bookshelf.urls')),

    url(r'^accounts/', include('allauth.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^selectable/', include('selectable.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
