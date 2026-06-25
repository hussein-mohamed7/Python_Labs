from django.contrib import admin

from .models import (
    Movie,
    Series,
    Category,
    Cast
)

admin.site.register(Movie)
admin.site.register(Series)
admin.site.register(Category)
admin.site.register(Cast)