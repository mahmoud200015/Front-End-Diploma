import requests
from bs4 import BeautifulSoup

# get an html webpage with requests
response = requests.get("https://books.toscrape.com/")
# print(response)

soup = BeautifulSoup(response.content, "html.parser")
# print(type(soup))

books = soup.find_all("article")
# print(books[0])

for index, book in enumerate(books):
    # get the title, rating, price of the book
    title = book.h3.a["title"]
    rating = book.p["class"][1]
    # Extract the price
    price_tag = book.find('p', class_='price_color')
    price = price_tag.text.strip() if price_tag else "Price not available"
    #print(price_tag)
    # print(price)

    # print both of them (title & rating with string interpolation)
    print(f"Book #{index + 1}\nTitle: {title}\nRating: {rating} stars\nPrice: {price}\n{'-' * 10}")

