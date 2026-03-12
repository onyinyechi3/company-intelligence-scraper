from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


def scrape_js_page():

    options = Options()
    options.add_argument("--headless")

    driver = webdriver.Chrome(options=options)

    url = "https://quotes.toscrape.com/js/"
    driver.get(url)

    time.sleep(3)

    quotes = driver.find_elements(By.CLASS_NAME, "quote")

    data = []

    for quote in quotes:
        text = quote.find_element(By.CLASS_NAME, "text").text
        author = quote.find_element(By.CLASS_NAME, "author").text

        data.append({
            "quote": text,
            "author": author
        })

    driver.quit()

    print(f"Extracted {len(data)} JS-rendered quotes")

    return data


if __name__ == "__main__":
    scrape_js_page()