from rest_framework import serializers
from .models import Product, Order


class OrderSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    quantity = serializers.IntegerField(min_value=1)

    class Meta:
        model = Order
        fields = ["product", "quantity"]
