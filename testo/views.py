from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import OrderSerializer
from .models import Order


class OrderAPIView(APIView):
    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        product = serializer.validated_data["product"]
        quantity = serializer.validated_data["quantity"]
        if product.stock < quantity:
            return Response({"error": "Out of stock"}, status=400)
        Order.objects.create(product=product, quantity=quantity)
        product.stock -= quantity
        product.save()
        return Response({"message": "dont"})

    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
