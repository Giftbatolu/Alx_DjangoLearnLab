# Delete:
**Command:** Delete the book you created and confirm the deletion by trying to retrieve all books again.

## Python command
```python
from bookshelf.models import Book

# Retrieve and delete the book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Confirm deletion
print(Book.objects.all())
```

## Expexted Output
```python
(<1>, {'bookshelf.Book': 1})
<QuerySet []>
```