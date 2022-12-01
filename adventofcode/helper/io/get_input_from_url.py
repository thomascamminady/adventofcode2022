import requests


def get_input_from_url(url: str) -> str:
    """Get input from url, using cookies"""

    # Get cookie from file
    with open("adventofcode/helper/io/cookie.txt", "r") as f:
        cookie = f.read()

    # Get input
    response = requests.get(url, cookies={"session": cookie})
    return response.text
