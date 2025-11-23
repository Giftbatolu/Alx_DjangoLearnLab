from rest_framework import ModelSerializer
from . models import Book

class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'