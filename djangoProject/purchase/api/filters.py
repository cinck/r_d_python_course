import django_filters

from purchase.models import Purchase


class PurchaseFilter(django_filters.FilterSet):
    class Meta:
        model = Purchase
        fields = {
            'user': ['exact'],
            'book': ['exact'],
        }