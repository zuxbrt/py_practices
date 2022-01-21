# Decode A Web Page Two

# Using the requests and BeautifulSoup Python libraries, print to the screen the full text of the article on this website: http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture.
# The article is long, so it is split up between 4 pages. Your task is to print out the text to the screen so that you can read the full article without having to click any buttons.

import requests
from bs4 import BeautifulSoup


def getContents(url):
    r = requests.get(url)
    r_html = r.text
    
    soup = BeautifulSoup(r_html, "html.parser")

    text_contents = soup.find_all("p", ["class:", 'paywall'])
    sections = []

    for item in text_contents:
        sections.append(item.text)

    return sections


def main():
    content = getContents('https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture')
    print(*content, sep = "\n")

main()
