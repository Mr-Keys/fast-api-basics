from fastapi import FastAPI
from enum import Enum

app = FastAPI()


@app.get('/')
def index():
    return {'message': 'Hello World'}


@app.get('/blog/all')
def get_all_blogs():
    return "all blogs"


class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'


@app.get('/blog/type/{type}')
def get_blog_from_type(type: BlogType):
    return {'message': f'BlogType: {BlogType[type].value}'}


@app.get('/blog/{id}')
def get_blog(id: int):
    return {'blog': f"Blog no {id}"}
