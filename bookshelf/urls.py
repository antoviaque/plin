
# Imports #########################################################################################

from django.conf.urls import patterns, url

from . import views


# URLs ############################################################################################

urlpatterns = patterns('bookshelf.views',
    url(r'^$', views.search, name='home'),
    url(r'^(?P<book_id>\d+)/$', views.detail, name='detail'),
)
