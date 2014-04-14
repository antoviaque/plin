from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'bookshelf.views.search', name='home'),
    url(r'^bookshelf/', include('bookshelf.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
