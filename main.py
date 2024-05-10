from fastapi import FastAPI
import uvicorn # for ASGI, Asynchronous Server Gateway Interface
import ollama
import requests
from bs4 import BeautifulSoup

#to create endpoints, llm is created and using llm we create all our endpoints
llm = FastAPI()

# index route opens automatically at http://127.0.0.1:8000
@llm.get('/')
def index():
    return {'message': 'Welcome to the API endpoint created by candidate Poornima Marasini'}


#web scraping to get the HTML tags of the product description:
 
req  = requests.get('https://webscraper.io/test-sites/e-commerce/ajax')

# we can check the status code of the website by using print(req.status_code).

# I tested the ouptut and the status code of the website before sending the get request.
soup = BeautifulSoup(req.content, 'html.parser')

# class="product-wrapper card-body" contains all the product description of all the products.
page = soup.find("div", class_="product-wrapper card-body")

input_html = page.prettify()


# An endpoint which uses the llama3 model that is locally installed using ollama.

@llm.get('/llma')
def get_res():
    response = ollama.generate(model="llama3",
                               prompt="using this HTMl content, please find the product name, description, price of product and store it in a JSON format"+ input_html,
                            format='json')
    return(response)


if __name__ == '__main__':
    uvicorn.run(llm, host='127.0.0.1', port=8000)


# to run the API, we type on the terminal
# conda run uvicorn poop:llm --reload