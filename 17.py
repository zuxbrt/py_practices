## Decode A Web Page

# Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage (http://www.nytimes.com/).

import requests
from bs4 import BeautifulSoup


def main():
    url = 'http://www.nytimes.com/'
    r = requests.get(url)
    r_html = r.text
    
    soup = BeautifulSoup(r_html, "html.parser")

    titles_h3 = soup.find_all("h3")
    titles = []

    for title in titles_h3:
        titles.append(title.text)

    print(*titles, sep = "\n")

main()
