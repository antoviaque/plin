
# Imports #########################################################################################

from django.conf.urls import include, patterns, url

from . import views


# URLs ############################################################################################

urlpatterns = patterns('bookshelf.views',
    url(r'^$', views.index, name='book_index'),
    url(r'^book/(?P<book_slug>[\w-]+)/$', views.book_detail, name='book_detail'),
    url(r'^rate/book/(?P<book_pk>\d+)/$', views.book_rate, name='book_rate'),
    url(r'^search/', include('haystack.urls')),
)
