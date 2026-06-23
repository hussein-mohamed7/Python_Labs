from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
import uuid

class Category(models.Model):
    name = models.CharField(max_length=80,validators=[MinLengthValidator(3)])

    def __str__(self):
        return self.name

class Book(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='books')
    title = models.CharField(max_length=200,validators=[MinLengthValidator(10)])
    desc = models.TextField()
    rate = models.FloatField()
    views = models.IntegerField(default=0)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title

class ISBN(models.Model):
    book = models.OneToOneField(Book,on_delete=models.CASCADE)
    author_title = models.CharField(max_length=200)
    book_title = models.CharField(max_length=200)
    isbn_number = models.CharField(max_length=100,unique=True,editable=False)

    def save(self,*args,**kwargs):
        if not self.isbn_number:
            self.isbn_number = str(uuid.uuid4())[:8]
        super().save(*args,**kwargs)

    def __str__(self):
        return self.isbn_number