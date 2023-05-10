class Bot:
    def __init__(self, name):
        self.name = name

    def say_name(self):
        print(f"Hi! My name is {self.name}")

    def send_message(self, message: str):
        print(message)


class TelegramBot(Bot):
    url = None
    chat_id = None

    def set_url(self, url: str):
        self.url = url

    def set_id(self, chat_id: str):
        self.chat_id = chat_id

    def send_message(self, message: str):
        print(
            f"Hello members of {self.chat_id} group!\n"
            f"Here is what I'd like to say:\n{message}\n"
            f"Message sent via {self.url}"
            )
        


