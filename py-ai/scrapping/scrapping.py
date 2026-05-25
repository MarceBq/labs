# scraper.py
import requests
import logging
from bs4 import BeautifulSoup


def get_book_prices(url, max_books=10):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "lxml")
        books = soup.find_all("article", class_="product_pod")

        results = []
        for book in books[:max_books]:
            title = book.find("h3").find("a")["title"]
            price_text = book.find("p", class_="price_color").text
            price = float(price_text.replace("£", "").replace("Â", "").strip())
            rating = book.find("p", class_="star-rating")["class"][1]

            results.append({"title": title, "price": price, "rating": rating})

        return results

    except requests.exceptions.RequestException as e:
        logging.error(f"Error scraping {url}: {e}")
        raise


def find_best_deals(books, max_price=15.0):
    good_ratings = ["Four", "Five"]
    return [b for b in books if b["price"] <= max_price and b["rating"] in good_ratings]


def find_cheapest(books):
    """Encuentra el libro más barato usando None como centinela."""
    cheapest = None
    for book in books:
        if cheapest is None or book["price"] < cheapest["price"]:
            cheapest = book
    return cheapest
