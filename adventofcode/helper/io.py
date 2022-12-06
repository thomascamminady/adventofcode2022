from typing import Any

import requests
from bs4 import BeautifulSoup
from bs4.element import Comment


def get_day(file: str) -> int:
    return int(file.split("/")[-1].split(".")[0])


def save_riddle_input(
    day: int, riddle: str, folder_prefix: str = "adventofcode/riddle_inputs"
) -> None:
    """Save riddle input to a file"""
    with open(f"{folder_prefix}/{day}.txt", "w") as f:
        f.write(riddle)


def get_riddle_input(day: int, year: int = 2022) -> str:
    url = f"https://adventofcode.com/{year}/day/{day}/input"
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


def tag_visible(element) -> bool:
    if element.parent.name in [
        "style",
        "script",
        "head",
        "title",
        "meta",
        "[document]",
    ]:
        return False
    if isinstance(element, Comment):
        return False
    return True


def text_from_html(body) -> str:
    soup = BeautifulSoup(body, "html.parser")
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)
    return " ".join(t.strip() for t in visible_texts)


def read_only_text_from_url(url: str) -> str:
    """Get input from url, without cookies"""
    # Get cookie from file
    with open("adventofcode/helper/cookie.txt", "r") as f:
        cookie = f.read()

    response = requests.get(url, cookies={"session": cookie})
    text = text_from_html(response.text)

    # throw everything away before the first occurence of the word Day
    text = text.split("Day", 1)[1]
    #  throw everything away after the text "Answer:"
    text = text.split("Answer:", 1)[0]
    return text


def submit_answer(day: int, level: int, answer: Any, year: int = 2022) -> None:
    # Get cookie from file
    with open("adventofcode/helper/cookie.txt", "r") as f:
        session_cookie = f.read()

    # The Advent of Code API endpoint for submitting solutions
    submit_url = f"https://adventofcode.com/{year}/day/{day}/answer"

    # Create the payload with your solution and the riddle input
    payload = {
        "level": f"{level}",  # The level number (1 or 2)
        "answer": str(answer),
        "session": session_cookie,
        "debug": "1",
    }

    # Send the HTTP POST request to the API endpoint with the payload
    response = requests.post(submit_url, json=payload)

    # Check the status code of the response to verify that the submission was successful
    if response.status_code == 200:
        print("Solution submitted successfully!")
    else:
        print("Failed to submit solution. Response status code: ", response.status_code)
