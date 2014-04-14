
# Imports #########################################################################################

from django.shortcuts import render, get_object_or_404

from bookshelf.models import Book


# Views ###########################################################################################

def book_search(request):
    book_list = Book.objects.all().order_by('-pub_date')[:10]
    context = {'book_list': book_list}
    return render(request, 'book/search.html', context)

def book_detail(request, book_pk):
    book = get_object_or_404(Book, pk=book_pk)
    context = {'book': book}
    return render(request, 'book/detail.html', context)
