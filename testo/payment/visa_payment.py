from .payment_strategy import PaymentStrategy


class VisaPayment(PaymentStrategy):
    def pay(self):
        print("visa")
