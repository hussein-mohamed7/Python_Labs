from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('', views.book_list, name='book_list'),

    path('create/', views.create_book, name='create_book'),

    path('update/<int:id>/', views.update_book, name='update_book'),

    path('delete/<int:id>/', views.delete_book, name='delete_book'),

    path('signup/', views.signup_view, name='signup'),

    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='books/login.html'
        ),
        name='login'
    ),

    path(
        'logout/',
        auth_views.LogoutView.as_view(),
        name='logout'
    ),
]