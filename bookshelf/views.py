
# Imports #########################################################################################

import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Book, Review
from .reviews import ReviewForm


# Views ###########################################################################################

def index(request):
    book_list = Book.objects.all().order_by('-pub_year', '-created')[:10]
    context = {'book_list': book_list}
    return render(request, 'book/index.html', context)

def book_detail(request, book_slug):
    book = get_object_or_404(Book, slug=book_slug)

    if request.user.is_authenticated():
        user = request.user
        try:
            review = Review.objects.get(user=user, book=book)
        except Review.DoesNotExist:
            review = Review(user=user, book=book)

        if request.method == 'POST':
            review_form = ReviewForm(request.POST, instance=review)
            if review_form.is_valid():
                review_form.save(commit=True)
        else:
            review_form = ReviewForm(instance=review)

    else:
        user = None
        review_form = None

    context = {
        'book': book,
        'book_user_rating': book.get_user_rating(request),
        'review_form': review_form,
        'reviews': Review.objects.filter(book=book).exclude(user=user).order_by('-created'),
    }
    return render(request, 'book/detail.html', context)

@login_required
def book_rate(request, book_pk):
    data = json.loads(request.body)
    book = get_object_or_404(Book, pk=book_pk)
    book.set_user_rating(request, data['rating'])

    context = {
        'overall_rating': book.overall_rating,
        'rating_votes': book.rating_votes,
    }
    return HttpResponse(json.dumps(context), content_type="application/json")
