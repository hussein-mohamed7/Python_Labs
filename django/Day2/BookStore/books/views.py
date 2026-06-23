from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm, SignUpForm

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, permission_required


def book_list(request):

    books = Book.objects.all()

    return render(
        request,
        'books/list.html',
        {'books': books}
    )


@login_required
def create_book(request):

    if request.method == 'POST':

        form = BookForm(request.POST)

        if form.is_valid():

            book = form.save(commit=False)
            book.user = request.user
            book.save()

            form.save_m2m()

            return redirect('book_list')

    else:
        form = BookForm()

    return render(
        request,
        'books/create.html',
        {'form': form}
    )


@login_required
def update_book(request, id):

    book = get_object_or_404(Book, id=id)

    if request.method == 'POST':

        form = BookForm(request.POST, instance=book)

        if form.is_valid():

            form.save()

            return redirect('book_list')

    else:
        form = BookForm(instance=book)

    return render(
        request,
        'books/update.html',
        {'form': form}
    )


@permission_required('books.delete_book')
def delete_book(request, id):

    book = get_object_or_404(Book, id=id)

    book.delete()

    return redirect('book_list')


def signup_view(request):

    if request.method == 'POST':

        form = SignUpForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            return redirect('book_list')

    else:
        form = SignUpForm()

    return render(
        request,
        'books/signup.html',
        {'form': form}
    )