from rest_framework import viewsets

from book.api.serializers import BookSerializer
from book.models import Book


class BookModelViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
