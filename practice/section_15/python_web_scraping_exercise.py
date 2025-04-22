import requests
import bs4
from typing import List


def take_quotes(url: str) -> List[str]:
    """
    Fetches all quotes from the given URL
    Args:
        url (str): The URL of the page to scrape.
    Returns:
        List[str]: A list of quote texts extracted from the page.
    """
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text, "lxml")

    # Select all span elements with class 'text'
    quotes = soup.select(".text")

    text_quotes = [quote.text for quote in quotes]
    return text_quotes


def take_head_tags(url: str) -> List[str]:
    """
    Fetches all tags from the given URL
    Args:
        url (str): The URL of the page to scrape.
    Returns:
        List[str]: A list of tags texts extracted from the page.
    """
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text, "lxml")

    head_tags_container = soup.select_one(".col-md-4.tags-box")

    if not head_tags_container:
        return []

    tags = head_tags_container.select(".tag")

    text_tags = [tag.text for tag in tags]
    return text_tags


working_path = "https://quotes.toscrape.com/"

quotes = take_quotes(working_path)
print("This are the home page quotes:")
print("\n".join(quotes))

print("\n")

tags = take_head_tags(working_path)
print("Here are the tags:")
print("\n".join(tags))
