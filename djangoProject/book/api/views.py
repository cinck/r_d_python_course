from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from book.api.serializers import BookSerializer
from book.models import Book
from book.api.filters import BookFilter


class BookModelViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    filterset_class = BookFilter
    search_fields = ['title', 'author']
    ordering_fields = ['author', 'title']
    ordering = ['author']