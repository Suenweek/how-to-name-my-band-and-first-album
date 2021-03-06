import re
import bs4
import requests


# FIXME: Add support for multiple languages.
RANDOM_ARTICLE_URL = 'https://ru.wikipedia.org/wiki/%D0%A1%D0%BB%D1%83%D0%B6%D0%B5%D0%B1%D0%BD%D0%B0%D1%8F:%D0%A1%D0%BB%D1%83%D1%87%D0%B0%D0%B9%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0'
RE_STRIP_HEADING = re.compile(r'([\w\d\-\s]+[\w\d]+)')


def get_random_article_heading():
    response = requests.get(RANDOM_ARTICLE_URL)
    soup = bs4.BeautifulSoup(response.content, 'lxml')
    heading = soup.select_one('#firstHeading')
    return heading.text


def strip_heading(heading):
    return RE_STRIP_HEADING.match(heading).groups()[0]


def get_random_band_name():
    heading = get_random_article_heading()
    return strip_heading(heading)


def get_random_first_album_name():
    heading = get_random_article_heading()
    return strip_heading(heading)
