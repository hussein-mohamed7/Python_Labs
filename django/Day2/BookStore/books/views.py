from django.shortcuts import render, redirect, get_object_or_404
from .models import Book

def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/list.html', {'books': books})


def create_book(request):
    if request.method == 'POST':
        Book.objects.create(
            title=request.POST['title'],
            desc=request.POST['desc'],
            rate=request.POST['rate'],
            views=request.POST['views']
        )
        return redirect('book_list')

    return render(request, 'books/create.html')



def update_book(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == 'POST':
        book.title = request.POST['title']
        book.desc = request.POST['desc']
        book.rate = request.POST['rate']
        book.views = request.POST['views']
        book.save()

        return redirect('book_list')

    return render(request, 'books/update.html', {'book': book})


def delete_book(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()

    return redirect('book_list')