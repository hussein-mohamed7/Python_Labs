from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('', views.book_list, name='book-list'),

    path('create/', views.book_create, name='book-create'),

    path('<int:book_id>/', views.book_detail, name='book-detail'),

    path('<int:book_id>/edit/', views.book_update, name='book-update'),

    path('<int:book_id>/delete/', views.book_delete, name='book-delete'),
]