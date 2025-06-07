class EmailHandler:
    def __init__(self):
        self.next_handler = None

    def set_next(self, handler):
        self.next_handler = handler
        return handler

    def handle(self, email):
        if self.next_handler:
            return self.next_handler.handle(email)
        return None


class SpamFilter(EmailHandler):
    def handle(self, email):
        subject_text = email["subject"].lower()
        body_text = email["body"].lower()

        if (
            "free" in subject_text
            or "win" in subject_text
            or "free" in body_text
            or "win" in body_text
        ):
            print("Email marked as spam")
            return
        else:
            super().handle(email)


class VirusFilter(EmailHandler):
    def handle(self, email):
        body_text = email["body"].lower()

        if "virus" in body_text:
            print("Email contains a virus")
            return
        else:
            super().handle(email)


class AutoResponder(EmailHandler):
    def handle(self, email):
        subject_text = email["subject"].lower()

        if "support" in subject_text or "help" in subject_text:
            print("Auto-responded to email")
            return
        else:
            super().handle(email)


class HumanResponder(EmailHandler):
    def handle(self, email):
        print("Email forwarded to human agent.")


spam = SpamFilter()
virus = VirusFilter()
auto = AutoResponder()
human = HumanResponder()

spam.set_next(virus).set_next(auto).set_next(human)

email1 = {"subject": "Win a FREE iPhone!", "body": "...", "from": "scammer@spam.com"}
email2 = {"subject": "URGENT: virus detected", "body": "This email contains a virus"}
email3 = {"subject": "Need help with my order", "body": "Order #12345"}
email4 = {"subject": "Just saying hi", "body": "How are you doing?"}

spam.handle(email1)
spam.handle(email2)
spam.handle(email3)
spam.handle(email4)
