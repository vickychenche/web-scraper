import requests
import sys
from bs4 import BeautifulSoup
# download url data


class ServerNotFound(Exception):
    """ raise when website server did not respond"""
    pass


def download_data(url):
    web_url = requests.get(url)
    if not web_url:
        print("ServerNotFound")
    else:
        soup = BeautifulSoup(web_url.text, 'html.parser')
        web_url.close()
        return soup
    return None


def get_title(soup):
    title_text = soup.title.get_text()
    print(title_text)
    return title_text


def get_content(soup):
    content_text = ''
    paragraphs = soup.find_all('p')
    for paragraph in paragraphs:
        content_text += paragraph.get_text()
        content_text += '\n'
    print(content_text)
    return content_text


if __name__ == "__main__":
    url = sys.argv[1]
    c = download_data(url)
    title = get_title(c)
    content = get_content(c)
