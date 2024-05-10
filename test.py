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

#The website called https://webscraper.io/test-sites is used which contains different types of website that are dynamic as well as static.

# I used E-commerce site with AJAX pagination links: 
#   the E-commerce site with multiple categories, subcategories. Dynamic links that use data without reloading the page for pagination, such that in this program
#   the scraped data, input_html  is different after every execution.
# The README.md contains the static as well as dynamic content examples and the outputs.

# The requests and BeautifulSoup library is used:
 
req  = requests.get('https://webscraper.io/test-sites/e-commerce/ajax')

# we can check the status code of the website by using print(req.status_code).

# I tested the ouptut and the status code of the website before sending the get request.
soup = BeautifulSoup(req.content, 'html.parser')

# The page was inspected and I found that the div class="product-wrapper card-body" contained all the product description of all the products.
page = soup.find("div", class_="product-wrapper card-body")

input_html = page.prettify()


# An endpoint which uses the llama3 model that is locally installed using ollama.
# Here we give the prompt and provide the input_html variable so that the output can be generated. 
@llm.get('/llma')
def get_res():
    response = ollama.generate(model="llama3",
                               prompt="using this HTMl content, please find the product name, description, price product and store it in a JSON format"+ input_html,
                            format='json')
    return(response)


# Running API with uvicorn
# to run the API, we type on the terminal
# conda run uvicorn poop:llm --reload
# if we run  http://127.0.0.1:8000/docs, then it provides the Postman type of UI
# called Swagger, where we can check the get,post and status code if the request is succesful or not

if __name__ == '__main__':
    uvicorn.run(llm, host='127.0.0.1', port=8000)
