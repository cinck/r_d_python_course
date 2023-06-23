import requests
import random


def random_url():
    urls = [
        "https://google.com",
        "https://facebook.com",
        "https://twitter.com",
        "https://amazon.com",
        "https://apple.com"
    ]
    return random.choice(urls)


if __name__ == "__main__":
    for _ in range(10):
        print(random_url())
