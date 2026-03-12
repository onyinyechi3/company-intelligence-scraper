import requests
from bs4 import BeautifulSoup

BASE_URL = "https://quotes.toscrape.com"


def scrape_quotes():

    data = []
    page = 1

    while True:

        url = f"{BASE_URL}/page/{page}/"
        print(f"Scraping page {page}...")

        response = requests.get(url)

        if response.status_code != 200:
            break

        soup = BeautifulSoup(response.text, "lxml")

        quotes = soup.find_all("div", class_="quote")

        if not quotes:
            break

        for quote in quotes:

            text = quote.find("span", class_="text").text.strip()
            author = quote.find("small", class_="author").text.strip()

            data.append({
                "quote": text,
                "author": author
            })

        page += 1

    return data