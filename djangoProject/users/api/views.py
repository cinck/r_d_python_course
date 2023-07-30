import django_filters.rest_framework as df
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter

from users.api.filters import UserFilter
from users.api.pagination import UserPagination
from users.api.serializers import UserSerializer
from users.models import User


class UserModelViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()

    serializer_class = UserSerializer

    pagination_class = UserPagination

    default_filter_backend = df.DjangoFilterBackend
    filter_backends = [default_filter_backend, SearchFilter, OrderingFilter]
    filterset_class = UserFilter
    search_fields = ['username', 'first_name', 'last_name']
    ordering_fields = ['first_name', 'last_name']
    ordering = ['first_name']
