from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
books = Book.objects.filter(author__name='author_name')
for book in books:
    print(book)

# List all books in a library
library = Library.objects.get(name='library_name')
for book in library.books.all():
    print(book)

#Retrieve the librarian of a library
librarian = Librarian.objects.get(library__name='library_name') 
print(librarian)