from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
def index(nome: str,sobrenome: str):
    return {'data':{'name':{nome}, 'sobrenome': {sobrenome}}}


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

@app.post('/blog')
def create_blog(request:Blog):
    return request
    return{'data':f'criando blog {title} e {body}'}



@app.get('/blog/{id}')
def show(id):
    return {'data':id, 'blog':f'{request.title}'}

@app.get('/blog/{id}/comments')
def comments(id:int, limit=10):
    if id > 10:
        return('error')
    return {'data':id, 'comments': f'comentário do id {id}'}

