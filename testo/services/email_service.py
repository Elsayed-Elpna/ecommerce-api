from .message_service import MessageService


class EmailService(MessageService):
    def send(self):
        print("Sending email")
