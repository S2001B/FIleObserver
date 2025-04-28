class Notifier:
    def send(self, message: str):
        raise NotImplementedError()


class EmailNotifier(Notifier):
    def send(self, message: str):
        print(f"Email sent: {message}")

class SMSNotifier(Notifier):
    def send(self, message: str):
        print(f"SMS sent: {message}")

class PushNotifier(Notifier):
    def send(self, message: str):
        print(f"Push notification: {message}")

def alert_all(notifiers: list[Notifier], msg: str):
    for object_send in notifiers:
        object_send.send(message=msg)

alert_all([EmailNotifier, SMSNotifier, PushNotifier], "System rebooted")