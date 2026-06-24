from ..models import Order, Product
from .email_service import EmailService
from .notification_service import NotificationService


class OrderService:
    def __init__(self, email_service, notification_service):
        self.email_service = email_service
        self.notification_service = notification_service

    def create_order(self, product, quantity):
        if product.stock < quantity:
            raise Exception("No enough stock")
        order = Order.objects.create(product=product, quantity=quantity)
        product.stock -= quantity
        product.save()
        self.email_service.send()
        self.notification_service.send()
        return order
