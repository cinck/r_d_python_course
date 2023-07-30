from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from purchase.api.filters import PurchaseFilter
from purchase.api.serializers import PurchaseSerializer
from purchase.models import Purchase


class PurchaseModelViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    filterset_class = PurchaseFilter
    ordering_fields = ['date']
    ordering = ['date']
