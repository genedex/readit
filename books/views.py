from django.shortcuts import render
from .models import Book
# Create your views here.
def list_books(request):
	books = Book.objects.exclude(date_reviewed__isnull = True)

	context = {
	'books': books,
	}

	return render(request, 'list.html', context )