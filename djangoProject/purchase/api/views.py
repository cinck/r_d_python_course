from rest_framework import viewsets

from purchase.api.serializers import PurchaseSerializer
from purchase.models import Purchase


class PurchaseModelViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
