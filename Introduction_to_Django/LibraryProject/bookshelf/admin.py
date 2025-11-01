from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('title', 'author', 'publication_year')

    # Fields to filter by in the right-hand sidebar
    list_filter = ('author', 'publication_year')

    # Fields searchable from the search bar at the top
    search_fields = ('title', 'author')

