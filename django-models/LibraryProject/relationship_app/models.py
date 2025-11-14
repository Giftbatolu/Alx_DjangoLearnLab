from django.db import models

class Author(models.Model):
    name = models.CharField(max_lenght=250)

class Book(models.Model):
    title = models.CharField(max_lenght=250)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

class Library(models.Model):
    name = models.CharField(max_lenght=250)
    books = models.ManyToManyField(Book, on_delete=models.CASCADE, related_name='library')

class Librarian(models.Model):
    name = models.CharField(max_lenght=250)
    library = OneToOneField(Library, on_delete=models.CASCADE)
