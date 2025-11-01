# Retrieve:
**Command:** Retrieve and display all attributes of the book you just created.

## Python command
```python
from bookshelf.models import Book

# Retrieve all books
books = Book.objects.all()
for b in books:
    print(b.id, b.title, b.author, b.publication_year)
```

## Expexted Output
```python
1 1984 George Orwell 1949
```