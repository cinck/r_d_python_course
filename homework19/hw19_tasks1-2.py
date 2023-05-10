class Bot:
    def __init__(self, name):
        self.name = name

    def say_name(self):
        print(f"Hi! My name is {self.name}!")

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
            f"{self.name} speaking in {self.chat_id} group and says:\n{message}\n"
            f"Message sent via {self.url}"
            )


if __name__ == "__main__":
    bot = Bot("PyBot")
    bot.say_name()
    bot.send_message("Greetings to all of you!")

    tg_bot = TelegramBot("TGbot")
    tg_bot.say_name()
    tg_bot.send_message("Greetings from TG bot!")
    tg_bot.set_id("PyChat")
    tg_bot.set_url("www.somepybotchat.url")
    print()
    tg_bot.send_message("Attributes have been set!")

