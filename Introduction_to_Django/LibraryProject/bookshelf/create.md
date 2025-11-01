# Create:
**Command:** Create a Book instance with the title “1984”, author “George Orwell”, and publication year 1949.

## Python command
```python
from bookshelf.models import Book

# Create a Book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
# Call the created instance
book
```

## Expexted Output
```python
<Book: 1984 by George Orwell (1949)>
```