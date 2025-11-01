# Create:
**Command:** Update the title of “1984” to “Nineteen Eighty-Four” and save the changes.

## Python command
```python
from bookshelf.models import Book

# Retrieve the existing book
book = Book.objects.get(title="1984")

# Update the title
book.title = "Nineteen Eighty-Four"
book.save()

# Verify update
print(book)
```

## Expexted Output
```python
Nineteen Eighty-Four by George Orwell (1949)
```