# <HW19> Task5. Create classes from Task 1 using type() function.
def constructor(self, name):
    self.name = name


TheBot = type(
    "Bot",
    (object,),
    {
        "__init__": lambda self, name: setattr(self, "name", name),
        "say_name": lambda self: print(f"Hi! My name is {self.name}"),
        "send_message": lambda self, message: print(message)
    })


def set_url(self, url: str):
    self.url = url


def set_id(self, chat_id: str):
    self.chat_id = chat_id


TheTGbot = type(
    "TheTGbot",
    (TheBot,),
    {
        "url": None,
        "chat_id": None,
        "set_url": set_url,
        "set_id": set_id,
        "send_message": lambda self, message: print(f"{self.name} speaking"
                                                    f" in {self.chat_id} group and says:\n{message}\n"
                                                    f"Message sent via {self.url}"
                                                    )
    }
)

if __name__ == "__main__":
    bot = TheBot("The_Bot")
    bot.say_name()
    bot.send_message("Greetings to all of you!")

    tg_bot = TheTGbot("TG_Bot")
    tg_bot.say_name()
    tg_bot.send_message("Greetings from TG bot!")
    tg_bot.set_id("PyChat")
    tg_bot.set_url("www.somepybotchat.url")
    print()
    tg_bot.send_message("Attributes have been set!")

