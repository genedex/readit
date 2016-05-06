from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from books.views import list_books
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'readit.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', list_books, name='books'),
)
