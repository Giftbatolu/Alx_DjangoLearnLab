from django.db import models

class Author(models.Model):
    name = models.CharField(max_lenght=250)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_lenght=250)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return f"{self.title} by {self.author.name}"

class Library(models.Model):
    name = models.CharField(max_lenght=250)
    books = models.ManyToManyField(Book, on_delete=models.CASCADE, related_name='library')

    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_lenght=250)
    library = OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} at {self.library.name}"
