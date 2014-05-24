
# Imports #########################################################################################

from django.conf.urls import patterns, url

from . import views


# URLs ############################################################################################

urlpatterns = patterns('bookshelf.views',
    url(r'^$', views.book_search, name='book_search'),
    url(r'^book/(?P<book_slug>[\w-]+)/$', views.book_detail, name='book_detail'),
    url(r'^rate/book/(?P<book_pk>\d+)/$', views.book_rate, name='book_rate'),
)
