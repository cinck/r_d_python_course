class Bot:
    """
    <HW19> Task1. Bot class.
    """
    def __init__(self, name):
        self.name = name

    def say_name(self):
        """
        Prints 'name' attribute
        :return:
        """
        print(f"Hi! My name is {self.name}!")

    def send_message(self, message: str):
        """
        Prints 'message' argument
        :param message: str()
        :return:
        """
        print(message)


class TelegramBot(Bot):
    """
    <HW19> Task2. Telegram bot class.
    """
    url = None
    chat_id = None

    def set_url(self, url: str):
        """
        Sets url ref to attribute
        :param url: str()
        :return:
        """
        self.url = url

    def set_id(self, chat_id: str):
        """
        Sets chad_id attribute.
        :param chat_id: str()
        :return:
        """
        self.chat_id = chat_id

    def send_message(self, message: str):
        """
        Prints message with additional comments
        :param message: str()
        :return:
        """
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

