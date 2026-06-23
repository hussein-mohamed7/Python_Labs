from django import forms
from .models import Book, Category
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'desc', 'rate', 'categories']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']