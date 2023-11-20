import requests
from bs4 import BeautifulSoup


def fetch_book_information(url):
    """
    Fetches book information (title, rating, and price) from the given URL.

    Args:
        url (str): The URL of the website to scrape.

    Returns:
        list: A list containing dictionaries with book information.
    """
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all articles containing book information
        books = soup.find_all("article")

        # Extract and store title, rating, and price for each book in a list of dictionaries
        book_information = []
        for book in books:
            title = book.h3.a["title"]
            rating = book.p["class"][1]

            # Extract the price
            price_tag = book.find('p', class_='price_color')
            price = price_tag.text.strip() if price_tag else "Price not available"

            book_info = {"Title": title, "Rating": rating, "Price": price}
            book_information.append(book_info)

        return book_information
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return []


def print_book_information(book_information):
    """
    Prints book information.

    Args:
        book_information (list): A list containing dictionaries with book information.
    """
    for book_info in book_information:
        print(f"Title: {book_info['Title']}")
        print(f"Rating: {book_info['Rating']}")
        print(f"Price: {book_info['Price']}\n")


if __name__ == "__main__":
    url = "https://books.toscrape.com/"

    # Fetch book information
    books_info = fetch_book_information(url)

    # Print book information
    print_book_information(books_info)
