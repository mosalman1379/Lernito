from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from lesson.models import Book
from lesson.serializer import BookSerializer, ChapterSerializer


class BookListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class ChapterListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = ChapterSerializer
    permission_classes = [IsAuthenticated]