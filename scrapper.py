import requests
from bs4 import BeautifulSoup
import json

# URL of the website to scrape
url = "https://books.toscrape.com/"

def scrape_book(url):
    response = requests.get(url)
    # print(response)                   # and to check the status ==> print(response.status_code),,,,, iif status is 200 then we can work
    # print(response.status_code)
    if response.status_code != 200:
        return
    response.encoding = response.apparent_encoding

    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_= "product_pod" )

    book_list = []

    for book in books:
        title = book.h3.a['title']
        price_text = book.find("p", class_="price_color").text
        currency = price_text[0]
        price = price_text[1:]

        book_data = {"title":title,"currency":currency, "price":price}
        book_list.append(book_data)

    #save to JSON file
    with open("books.json", "w", encoding="utf-8") as f:
        json.dump(book_list, f, ensure_ascii = False, indent=4)

        print(f"saved {len(book_list)} books to books.json")


scrape_book(url)