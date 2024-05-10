import requests
from bs4 import BeautifulSoup

req  = requests.get('https://webscraper.io/test-sites/e-commerce/ajax')
print(req.status_code)

soup = BeautifulSoup(req.content, 'html.parser')
page = soup.find("div", class_="product-wrapper card-body")
print(page.prettify())

