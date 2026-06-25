from .payment_strategy import PaymentStrategy


class CashPayment(PaymentStrategy):

    def pay(self):
        print("Paying with Cash")
