from django.shortcuts import render
from rest_framework import generics.ListAPIView
from .models import Book
from .serializers import BookSerializer
from rest_framework.viewsets.ModelViewSet import ModelViewSet
from rest_framework import permissions

class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]