from rest_framework import serializers
from .models import Author, Book
import datetime

# Author Serializer with nested Book Serializer
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = ['id', 'name', 'books']

# Book Serializer with publication year validation
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']
# Check if publication is not in the future
    def validate_publication_year(self, publication_year):
        current_year = datetime.datetime.now().year
        if publication_year > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return publication_year