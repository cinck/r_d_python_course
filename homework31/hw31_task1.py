# <HW31> Task1: Request to random web-site and print response details.

import requests
import random


def random_url():
    """Returns random URL from list"""
    urls = [
        "https://google.com",
        "https://facebook.com",
        "https://twitter.com",
        "https://amazon.com",  # never responds for some reason
        "https://apple.com"
    ]
    return random.choice(urls)


def get_response_from_url(url: str):
    """Returns request.get() object if connection successful"""
    try:
        result = requests.get(url=url)
    except Exception:
        return None
    return result


def show_response_from(url: str):
    """
    Prints HTTP response data as per homework task
    :param url: URL
    :return:
    """
    print(url)
    response = get_response_from_url(url)
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
