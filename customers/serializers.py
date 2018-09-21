from rest_framework import serializers
from .models import Customer, LANGUAGE_CHOICES, STYLE_CHOICES


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ('id', 'first_name', 'last_name', 'purchase_item',
                  'price_total', )