from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from books.views import list_books, AuthorList, BookDetail, AuthorDetail
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'readit.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', list_books, name='books'),
    url(r'^authors/$',AuthorList.as_view(), name = 'authors'),
    url(r'^books/(?P<pk>[-\w]+)/$', BookDetail.as_view(), name = 'book-detail'),
    url(r'^authors/(?P<pk>[-\w]+)/$', AuthorDetail.as_view(), name = 'author-detail')
)
