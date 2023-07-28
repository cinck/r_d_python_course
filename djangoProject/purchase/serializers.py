from rest_framework import serializers

from purchase.models import Purchase


class PurchaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Purchase
        fields = ('date', 'user', 'book')
        read_only_fields = ('date',)