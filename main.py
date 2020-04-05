from fastapi import FastAPI
app = FastAPI()

from pydantic import BaseModel

@app.get('/')
def hello_world():
    return {"message": "Hello World during the coronavirus pandemic!"}


class HelloNameResp(BaseModel):
    message: str

@app.get('/hello/{name}', response_model=HelloNameResp)
def hello_name(name: str):
    return HelloNameResp(message= f"Hello {name}")

@app.get('/method')
def get_method():
    return {"method":"GET"}

@app.put('/method')
def put_method():
    return {"method":"PUT"}

@app.delete('/method')
def delete_method():
    return {"method":"DELETE"}

@app.post('/method')
def post_method():
    return {"method":"POST"}