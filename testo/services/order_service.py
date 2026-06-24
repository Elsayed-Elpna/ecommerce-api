from ..models import Order, Product
from .email_service import EmailService
from .notification_service import NotificationService


class OrderService:
    def __init__(self, services):
        self.services = services

    def create_order(self, product, quantity):
        if product.stock < quantity:
            raise Exception("No enough stock")
        order = Order.objects.create(product=product, quantity=quantity)
        product.stock -= quantity
        product.save()
        for service in self.services:
            service.send()
        return order
