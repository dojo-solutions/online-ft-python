from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.books_index, name="books_index"),
    url(r'^books/create/$', views.books_create, name="books_create"),
    url(r'^books/(?P<book_id>\d+)/$', views.books_show, name="books_show"),
    url(r'^books/(?P<book_id>\d+)/add_author$', views.add_author, name="add_author"),
    url(r'^authors/$', views.authors_index, name="authors_index"),
    url(r'^authors/create/$', views.authors_create, name="authors_create"),
    url(r'^authors/(?P<author_id>\d+)/$', views.authors_show, name="authors_show"),
    url(r'^authors/(?P<author_id>\d+)/add_book$', views.add_book, name="add_book"),
]