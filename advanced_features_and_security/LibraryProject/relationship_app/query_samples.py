from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
author = Author.objects.get(name=author_name)
books = Book.objects.filter(author=author)
for book in books:
    print(book)

# List all books in a library
library = Library.objects.get(name=library_name)
for book in library.books.all():
    print(book)

#Retrieve the librarian of a library
library = Library.objects.get(name=library_name)
librarian = Librarian.objects.get(library=library) 
print(librarian)