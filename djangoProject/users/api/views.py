from rest_framework import viewsets

from users.api.pagination import UserPagination
from users.api.serializers import UserSerializer
from users.models import User


class UserModelViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = UserPagination
