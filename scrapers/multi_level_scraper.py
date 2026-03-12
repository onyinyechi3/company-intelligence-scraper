import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

BASE_URL = "https://books.toscrape.com/"


def get_soup(url):
    response = requests.get(url)
    response.raise_for_status()
    return BeautifulSoup(response.text, "lxml")


def scrape_book_details(book_url, category_name):
    soup = get_soup(book_url)

    title = soup.find("div", class_="product_main").find("h1").get_text(strip=True)
    price = soup.find("p", class_="price_color").get_text(strip=True)
    availability = soup.find("p", class_="instock availability").get_text(strip=True)

    rating_tag = soup.find("p", class_="star-rating")
    rating_classes = rating_tag.get("class", [])
    rating = rating_classes[1] if len(rating_classes) > 1 else "Unknown"

    return {
        "category": category_name,
        "title": title,
        "price": price,
        "availability": availability,
        "rating": rating,
        "book_url": book_url,
    }


def scrape_category(category_url, category_name):
    data = []
    next_page = category_url

    while next_page:
        print(f"Scraping category page: {next_page}")
        soup = get_soup(next_page)

        articles = soup.find_all("article", class_="product_pod")

        for article in articles:
            link = article.find("h3").find("a")
            relative_book_url = link.get("href")
            book_url = urljoin(next_page, relative_book_url)

            book_data = scrape_book_details(book_url, category_name)
            data.append(book_data)

        next_button = soup.find("li", class_="next")
        if next_button:
            next_link = next_button.find("a").get("href")
            next_page = urljoin(next_page, next_link)
        else:
            next_page = None

    return data


def scrape_all_categories(limit=5):
    soup = get_soup(BASE_URL)
    category_links = soup.select("div.side_categories ul li ul li a")

    all_data = []

    for category in category_links[:limit]:
        category_name = category.get_text(strip=True)
        category_href = category.get("href")
        category_url = urljoin(BASE_URL, category_href)

        print(f"\nStarting category: {category_name}")
        category_data = scrape_category(category_url, category_name)
        all_data.extend(category_data)

    return all_data