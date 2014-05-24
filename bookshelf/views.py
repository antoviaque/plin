
# Imports #########################################################################################

import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from bookshelf.models import Book


# Views ###########################################################################################

def book_search(request):
    book_list = Book.objects.all().order_by('-pub_date')[:10]
    context = {'book_list': book_list}
    return render(request, 'book/search.html', context)

def book_detail(request, book_pk):
    book = get_object_or_404(Book, pk=book_pk)
    context = {
        'book': book,
        'book_rating': book.rating.get_rating(),
        'book_nb_votes': book.rating_votes,
        'book_user_rating': book.get_user_rating(request),
    }
    return render(request, 'book/detail.html', context)

@login_required
def book_rate(request, book_pk):
    data = json.loads(request.body)
    book = get_object_or_404(Book, pk=book_pk)
    book.set_user_rating(request, data['rating'])
    return HttpResponse(json.dumps({}), content_type="application/json")
