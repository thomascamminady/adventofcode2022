import requests


def get_riddle_input(file: str) -> str:
    file_name = file.split("/")[-1]
    day = int(file_name.split(".")[0])
    url = f"https://adventofcode.com/2022/day/{day}/input"
    riddle_input = get_text_from_url(url)
    return riddle_input


def get_text_from_url(url: str) -> str:
    """Get input from url, using cookies"""

    # Get cookie from file
    with open("adventofcode/helper/cookie.txt", "r") as f:
        cookie = f.read()

    # Get input
    response = requests.get(url, cookies={"session": cookie})
    return response.text
