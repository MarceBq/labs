# test_scraper.py
import json
from scrapping import get_book_prices, find_best_deals, find_cheapest

OUTPUT_FILE = "books_report.json"


def main():
    print("Scrapeando páginas...\n")

    all_books = []
    for page_num in range(1, 4):
        url = f"https://books.toscrape.com/catalogue/page-{page_num}.html"
        books = get_book_prices(url=url, max_books=10)
        all_books.extend(books)
        print(f"  Página {page_num}: {len(books)} libros obtenidos")

    print(f"\nTotal: {len(all_books)} libros\n")
    print(f"{'Título':<45} {'Precio':>8}  {'Rating'}")
    print("-" * 65)
    for book in all_books:
        print(f"{book['title']:<45} £{book['price']:>6.2f}  {book['rating']}")

    deals = find_best_deals(all_books, max_price=15.0)
    print(f"\nMejores ofertas (<=£15, rating alto): {len(deals)}")
    for deal in deals:
        print(f"  -> {deal['title']} — £{deal['price']}")

    cheapest = find_cheapest(all_books)
    print(f"\nLibro más barato: {cheapest['title']} — £{cheapest['price']}")

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(all_books, f, indent=2, ensure_ascii=False)
    print(f"\nGuardado en: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
