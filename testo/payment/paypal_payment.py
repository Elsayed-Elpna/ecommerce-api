from .payment_strategy import PaymentStrategy


class PaypalPayment(PaymentStrategy):

    def pay(self):
        print("Paying with Paypal")
