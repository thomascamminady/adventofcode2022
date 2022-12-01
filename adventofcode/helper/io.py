import requests
from bs4 import BeautifulSoup
from bs4.element import Comment


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


def tag_visible(element):
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


def text_from_html(body):
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
