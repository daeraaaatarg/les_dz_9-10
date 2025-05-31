import requests
from bs4 import BeautifulSoup

base_url = "http://books.toscrape.com/catalogue/page-{}.html"
book_titles = []

for page in range(1, 51):
    url = base_url.format(page)
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    h3_tags = soup.find_all('h3')

    for h3 in h3_tags:
        title = h3.find('a')['title']
        book_titles.append(title)

for i, title in enumerate(book_titles, 1):
    print(f"{i}. {title}")