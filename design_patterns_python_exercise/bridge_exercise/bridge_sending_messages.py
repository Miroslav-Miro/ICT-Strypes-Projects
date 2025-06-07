from abc import ABC, abstractmethod


class MessageSender(ABC):
    @abstractmethod
    def send_message(self, content):
        pass


class EmailSender(MessageSender):
    def send_message(self, content):
        print(f"Sending '{content}' via Email")


class SMSSender(MessageSender):
    def send_message(self, content):
        print(f"Sending '{content}' via SMS")


class PushNotificationSender(MessageSender):
    def send_message(self, content):
        print(f"Sending '{content}' via PushNotification")


class Message:
    def __init__(self, sender: MessageSender):
        self.sender = sender

    def send(self, content):
        pass


class AlertMessage(Message):
    def send(self, content):
        return self.sender.send_message(f"{content} as an alert")


class NotificationMessage(Message):
    def send(self, content):
        return self.sender.send_message(f"{content} as an notification")


class ReportMessage(Message):
    def send(self, content):
        return self.sender.send_message(f"{content} as an report")


email = EmailSender()
sms = SMSSender()
push = PushNotificationSender()

alert = AlertMessage(email)
notification = NotificationMessage(push)
report = ReportMessage(sms)

alert.send("High CPU usage")
notification.send("New message received")
report.send("Weekly report ready")
