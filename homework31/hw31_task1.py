import requests
import random
import json


def random_url():
    urls = [
        "https://google.com",
        "https://facebook.com",
        "https://twitter.com",
        "https://amazon.com",  # never responds for some reason
        "https://apple.com"
    ]
    return random.choice(urls)


def get_response_from(url: str):
    try:
        result = requests.get(url=url)
    except Exception:
        return None
    return result


def show_response_from(url: str):
    print(url)
    response = get_response_from(url)
    if not response:
        print("Failed to connect")
    else:
        html_len = len(response.text)
        print(response)
        print(f"HTML code lengths: {html_len} characters")


if __name__ == "__main__":
    for _ in range(10):
        show_response_from(random_url())
        print("---------------------------------------------")
