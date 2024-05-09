from fastapi import FastAPI
import uvicorn
from product_info import ProductInfo
import ollama

llm = FastAPI()

# index route opens automatically at http://127.0.0.1:8000
@llm.get('/')
def index():
    return {'message': 'Hello Poopu boi'}

@llm.get('/naming')
def get_name(name: str):
    return {'name': 'Hello, my name is'f'{name}'}

@llm.get('/llma')
def get_res():
    response = ollama.generate(model='llama3',
                               prompt='hello')
    print(response['response'])
# @llm.post('/llama3_prediction')
# def predict_values(data:ProductInfo):
#     data = data.model_dump()
#     ollama_response = ollama.create(

#     )





# Running API with uvicorn

if __name__ == '__main__':
    uvicorn.run(llm, host='127.0.0.1', port=8000)


# to run the API, we type on the terminal
# conda run uvicorn poop:llm --reload



# if we run  http://127.0.0.1:8000/docs, then it provides the Postman type of UI
# called Swagger, where we can check the post and status code if the request is succesful or not
