# Retrieve:
**Command:** Retrieve and display all attributes of the book you just created.

## Python command
```python
from bookshelf.models import Book

# Retrieve all books
books = Book.objects.get(title=1984)
print(f"{book.title} by {book.author} published in year {book.publication_year}")
```

## Expexted Output
```python
1984 by George Orwell published in year 1949
```