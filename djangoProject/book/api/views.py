from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
import django_filters.rest_framework as df

from book.api.serializers import BookSerializer
from book.models import Book
from book.api.filters import BookFilter


class BookModelViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    default_filter_backend = df.DjangoFilterBackend
    filter_backends = [default_filter_backend, SearchFilter, OrderingFilter]
    filterset_class = BookFilter
    search_fields = ['title', 'author']
    ordering_fields = ['author', 'title']
    ordering = ['author']