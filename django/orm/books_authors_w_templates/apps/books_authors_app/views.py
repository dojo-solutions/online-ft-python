from django.shortcuts import render, redirect
from .models import Book, Author

# Create your views here.
def books_index(req):
    context = {
        "books": Book.objects.all()
    }
    return render(req, 'books_authors_app/books_index.html', context)

def books_create(req):
    Book.objects.create(
        title=req.POST['title'],
        desc=req.POST['desc']
    )
    return redirect('/')

def books_show(req, book_id):
    context = {
        "book": Book.objects.get(id=book_id),
        "other_authors": Author.objects.exclude(books=book_id)
    }
    return render(req, 'books_authors_app/books_show.html', context)

def add_author(req, book_id):
    book = Book.objects.get(id=book_id)
    author = Author.objects.get(id=req.POST['author'])
    book.authors.add(author)
    return redirect(f"/books/{book_id}")

def authors_index(req):
    context = {
        "authors": Author.objects.all()
    }
    return render(req, 'books_authors_app/authors_index.html', context)

def authors_create(req):
    Author.objects.create(
        first_name=req.POST["first_name"],
        last_name=req.POST["last_name"],
        notes=req.POST["notes"],
    )
    return redirect('/authors')

def authors_show(req, author_id):
    context = {
        "author": Author.objects.get(id=author_id),
        "other_books": Book.objects.exclude(authors=author_id)
    }
    return render(req, 'books_authors_app/authors_show.html', context)

def add_book(req, author_id):
    author = Author.objects.get(id=author_id)
    book = Book.objects.get(id=req.POST['book'])
    book.authors.add(author)
    return redirect(f"/authors/{author_id}")