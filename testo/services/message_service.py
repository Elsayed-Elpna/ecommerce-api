from abc import ABC, abstractmethod


class MessageService(ABC):
    @abstractmethod
    def send(self):
        pass
