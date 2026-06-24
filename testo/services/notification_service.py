from .message_service import MessageService


class NotificationService(MessageService):
    def send(self):
        print("Sending notifitions")
