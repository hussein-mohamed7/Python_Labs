from django.contrib import admin
from .models import Book, Category, ISBN


class ISBNInline(admin.StackedInline):
    model = ISBN
    extra = 0


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'rate',
        'views',
        'user'
    )

    list_filter = (
        'rate',
        'categories'
    )

    search_fields = (
        'title',
    )

    inlines = [ISBNInline]


admin.site.register(Category)