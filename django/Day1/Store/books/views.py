from django.shortcuts import render, redirect

book_list_data = [
    {
        'id': 1,
        'title': 'Python Basics',
        'author': 'Hussein',
        'price': 1000
    },
    {
        'id': 2,
        'title': 'Django Guide',
        'author': 'Hassan',
        'price': 2000
    }
]


def get_book(book_id):
    for book in book_list_data:
        if book['id'] == book_id:
            return book
    return None


def book_list(request):
    context = {
        'books': book_list_data
    }

    return render(
        request,
        'books/book_list.html',
        context
    )


def book_detail(request, book_id):

    book = get_book(book_id)

    context = {
        'book': book
    }

    return render(
        request,
        'books/book_detail.html',
        context
    )


def book_create(request):

    if request.method == 'POST':

        new_book = {
            'id': len(book_list_data) + 1,
            'title': request.POST.get('title'),
            'author': request.POST.get('author'),
            'price': request.POST.get('price')
        }

        book_list_data.append(new_book)

        return redirect('books:book-list')

    return render(
        request,
        'books/book_form.html'
    )


def book_update(request, book_id):

    book = get_book(book_id)

    if request.method == 'POST':

        book['title'] = request.POST.get('title')
        book['author'] = request.POST.get('author')
        book['price'] = request.POST.get('price')

        return redirect('books:book-list')

    return render(
        request,
        'books/book_form.html',
        {'book': book}
    )


def book_delete(request, book_id):

    book = get_book(book_id)

    if book:
        book_list_data.remove(book)

    return redirect('books:book-list')